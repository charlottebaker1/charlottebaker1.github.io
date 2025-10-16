// contact.js
//final fix to send email with no redirect
document.addEventListener("DOMContentLoaded", () => {

  const form =
    document.getElementById("contact-form") ||
    document.querySelector('form[action*="web3forms"]') ||
    document.querySelector("form");

  if (!form) return;
  let result = document.getElementById("contact-result");
  if (!result) {
    result = document.createElement("p");
    result.id = "contact-result";
    result.className = "muted";
    result.style.marginTop = "8px";
    form.appendChild(result);
  }

  form.addEventListener(
    "submit",
    async (e) => {
      e.preventDefault();

      if (!form.checkValidity()) {
        form.reportValidity();
        return;
      }

      const bot = form.querySelector('[name="botcheck"]');
      if (bot && bot.checked) {
        result.textContent = "Spam detected.";
        return;
      }

      result.style.display = "block";
      result.textContent = "Sending…";

      try {
        const fd = new FormData(form);

        const response = await fetch("https://api.web3forms.com/submit", {
          method: "POST",
          headers: { Accept: "application/json" }, 
          body: fd,
          redirect: "follow", 
        });

        const data = await response.json();

        if (response.ok && (data.success === true || data.status === 200)) {
          result.textContent = "Thanks! Your message has been sent.";
          form.reset();
        } else {
          result.textContent =
            data.message || "There was a problem sending your message.";
        }
      } catch (err) {
        console.error(err);
        result.textContent = "Something went wrong. Please try again.";
      }

      setTimeout(() => (result.style.display = "none"), 4000);
    },
    true 
  );
});
