/*
 * Voice agent ("Nova") interactions for nathanscottlester.com
 * - copyPhone(): copies the toll-free number and shows the toast
 * - openVoiceAgentModal() / closeVoiceAgentModal(): native <dialog> control
 * - startWebVoiceCall() / endWebVoiceCall(): Retell AI WebRTC call
 *
 * The Retell SDK is lazy-loaded as an ES module only after the backend issues
 * an access token, so pages pay no SDK cost unless a visitor starts a call.
 * If the backend is unavailable, the modal degrades to the direct-dial number.
 */
(function () {
  "use strict";

  var PHONE_E164 = "+18886003783";
  var PHONE_DISPLAY = "+1 (888) 600-3783";
  var WEB_CALL_ENDPOINT = "https://voice.lesterlabs.cloud/api/v1/retell/create-web-call";
  var RETELL_SDK_URL = "https://esm.sh/retell-client-js-sdk@2";

  var retellClient = null;
  var isCallActive = false;

  function el(id) {
    return document.getElementById(id);
  }

  function dialLinkHtml() {
    return '<a href="tel:' + PHONE_E164 + '" class="phone-link">' + PHONE_DISPLAY + "</a>";
  }

  function copyPhone(btn) {
    navigator.clipboard.writeText(PHONE_E164).then(function () {
      var toast = btn.querySelector(".copy-toast");
      if (toast) {
        toast.classList.add("visible");
        setTimeout(function () { toast.classList.remove("visible"); }, 2200);
      }
    });
  }

  function openVoiceAgentModal() {
    var dialog = el("voice-agent-modal");
    if (!dialog || dialog.open) return;
    dialog.showModal();
  }

  function closeVoiceAgentModal() {
    var dialog = el("voice-agent-modal");
    if (dialog && dialog.open) dialog.close();
  }

  function setIdleUi(statusHtml) {
    var orb = el("voice-orb");
    var statusEl = el("voice-status");
    var startBtn = el("btn-start-call");
    var endBtn = el("btn-end-call");
    if (orb) orb.classList.remove("active", "connecting");
    if (statusEl && statusHtml) statusEl.innerHTML = statusHtml;
    if (startBtn) { startBtn.hidden = false; startBtn.disabled = false; }
    if (endBtn) endBtn.hidden = true;
  }

  function handleCallEnded() {
    isCallActive = false;
    retellClient = null;
    setIdleUi("Call ended. Thank you for testing Nova!");
  }

  function showFallback(reason) {
    console.warn("Voice web call unavailable:", reason);
    isCallActive = false;
    retellClient = null;
    setIdleUi(
      "Browser calling is temporarily unavailable.<br><strong>Dial Nova directly: " +
        dialLinkHtml() +
        "</strong>"
    );
  }

  async function startWebVoiceCall() {
    var statusEl = el("voice-status");
    var orb = el("voice-orb");
    var startBtn = el("btn-start-call");
    var endBtn = el("btn-end-call");

    statusEl.textContent = "Connecting to Retell AI voice gateway...";
    startBtn.disabled = true;
    orb.classList.add("connecting");

    try {
      var response = await fetch(WEB_CALL_ENDPOINT, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ client_id: "nathan-lester" })
      });
      if (!response.ok) throw new Error("Backend responded " + response.status);
      var data = await response.json();
      if (!data || !data.access_token) throw new Error("No access token returned");

      var sdk = await import(RETELL_SDK_URL);
      retellClient = new sdk.RetellWebClient();

      retellClient.on("call_started", function () {
        isCallActive = true;
        orb.classList.remove("connecting");
        orb.classList.add("active");
        statusEl.textContent = "Nova is listening... speak into your microphone.";
        startBtn.hidden = true;
        endBtn.hidden = false;
      });
      retellClient.on("call_ended", handleCallEnded);
      retellClient.on("error", function (err) {
        console.error(err);
        if (retellClient) retellClient.stopCall();
        showFallback(err);
      });

      await retellClient.startCall({ accessToken: data.access_token });
    } catch (err) {
      showFallback(err);
    }
  }

  function endWebVoiceCall() {
    if (retellClient) retellClient.stopCall();
    handleCallEnded();
  }

  function initDialog() {
    var dialog = el("voice-agent-modal");
    if (!dialog) return;

    // Hang up whenever the dialog closes (Esc, close button, light dismiss).
    dialog.addEventListener("close", function () {
      if (isCallActive || retellClient) endWebVoiceCall();
    });

    // Light-dismiss fallback where <dialog closedby="any"> is unsupported (e.g. Safari).
    if (!("closedBy" in HTMLDialogElement.prototype)) {
      var outside = function (e) {
        var r = dialog.getBoundingClientRect();
        return e.clientX < r.left || e.clientX > r.right || e.clientY < r.top || e.clientY > r.bottom;
      };
      var pressedOutside = false;
      dialog.addEventListener("pointerdown", function (e) { pressedOutside = outside(e); });
      dialog.addEventListener("pointerup", function (e) {
        if (pressedOutside && outside(e)) dialog.close();
      });
    }
  }

  window.copyPhone = copyPhone;
  window.openVoiceAgentModal = openVoiceAgentModal;
  window.closeVoiceAgentModal = closeVoiceAgentModal;
  window.startWebVoiceCall = startWebVoiceCall;
  window.endWebVoiceCall = endWebVoiceCall;

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", initDialog);
  } else {
    initDialog();
  }
})();
