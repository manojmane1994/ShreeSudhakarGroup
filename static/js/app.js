/**
 * Shree Sudhakar Group - Interactive Client Script
 */

document.addEventListener("DOMContentLoaded", () => {
  // 1. Mobile Menu Toggle
  const menuBtn = document.getElementById("mobile-menu-btn");
  const mobileMenu = document.getElementById("mobile-menu");

  if (menuBtn && mobileMenu) {
    menuBtn.addEventListener("click", () => {
      mobileMenu.classList.toggle("hidden");
    });

    // Close mobile menu when a nav link is clicked
    mobileMenu.querySelectorAll("a").forEach(link => {
      link.addEventListener("click", () => {
        mobileMenu.classList.add("hidden");
      });
    });
  }

  // 2. Enquiry Modal Handlers
  const enquiryModal = document.getElementById("enquiry-modal");
  const openModalBtns = document.querySelectorAll(".open-enquiry-modal");
  const closeModalBtns = document.querySelectorAll(".close-enquiry-modal");

  openModalBtns.forEach(btn => {
    btn.addEventListener("click", (e) => {
      e.preventDefault();
      const preselectVertical = btn.getAttribute("data-vertical");
      if (preselectVertical) {
        const modalSelect = document.getElementById("modal-vertical");
        if (modalSelect) modalSelect.value = preselectVertical;
      }
      if (enquiryModal) {
        enquiryModal.classList.remove("hidden");
        enquiryModal.classList.add("flex");
        document.body.style.overflow = "hidden";
      }
    });
  });

  closeModalBtns.forEach(btn => {
    btn.addEventListener("click", () => {
      if (enquiryModal) {
        enquiryModal.classList.add("hidden");
        enquiryModal.classList.remove("flex");
        document.body.style.overflow = "auto";
      }
    });
  });

  // Close modal on backdrop click
  if (enquiryModal) {
    enquiryModal.addEventListener("click", (e) => {
      if (e.target === enquiryModal) {
        enquiryModal.classList.add("hidden");
        enquiryModal.classList.remove("flex");
        document.body.style.overflow = "auto";
      }
    });
  }

  // 3. Form Submission Handlers (Page form & Modal form)
  setupForm("page-enquiry-form", "page-form-feedback", "page-submit-btn");
  setupForm("modal-enquiry-form", "modal-form-feedback", "modal-submit-btn");
});

/**
 * Configure AJAX submission for an enquiry form
 */
function setupForm(formId, feedbackId, submitBtnId) {
  const form = document.getElementById(formId);
  const feedback = document.getElementById(feedbackId);
  const submitBtn = document.getElementById(submitBtnId);

  if (!form) return;

  form.addEventListener("submit", async (e) => {
    e.preventDefault();

    const formData = new FormData(form);
    const payload = {
      name: formData.get("name")?.trim(),
      mobile: formData.get("mobile")?.trim(),
      email: formData.get("email")?.trim() || null,
      vertical: formData.get("vertical")?.trim() || "Government Projects",
      city: formData.get("city")?.trim() || null,
      message: formData.get("message")?.trim() || null
    };

    // Validation
    if (!payload.name || payload.name.length < 2) {
      showFeedback(feedback, "Please enter your full name.", "error");
      return;
    }
    if (!payload.mobile || payload.mobile.length < 8) {
      showFeedback(feedback, "Please enter a valid mobile number.", "error");
      return;
    }

    // Button loading state
    const originalBtnText = submitBtn.innerHTML;
    submitBtn.disabled = true;
    submitBtn.innerHTML = `
      <svg class="animate-spin -ml-1 mr-2 h-5 w-5 text-white inline-block" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24">
        <circle class="opacity-25" cx="12" cy="12" r="10" stroke="currentColor" stroke-width="4"></circle>
        <path class="opacity-75" fill="currentColor" d="M4 12a8 8 0 018-8V0C5.373 0 0 5.373 0 12h4zm2 5.291A7.962 7.962 0 014 12H0c0 3.042 1.135 5.824 3 7.938l3-2.647z"></path>
      </svg> Submitting...
    `;

    try {
      const response = await fetch("/api/enquiry", {
        method: "POST",
        headers: {
          "Content-Type": "application/json"
        },
        body: JSON.stringify(payload)
      });

      const result = await response.json();

      if (response.ok && result.success) {
        showFeedback(feedback, result.message || "Thank you! Your enquiry has been received.", "success");
        form.reset();

        // If in modal, close after 3 seconds
        if (formId === "modal-enquiry-form") {
          setTimeout(() => {
            const modal = document.getElementById("enquiry-modal");
            if (modal) {
              modal.classList.add("hidden");
              modal.classList.remove("flex");
              document.body.style.overflow = "auto";
              feedback.classList.add("hidden");
            }
          }, 3000);
        }
      } else {
        const errMsg = result.detail || result.message || "Something went wrong. Please call us directly at +91 9689820892.";
        showFeedback(feedback, errMsg, "error");
      }
    } catch (err) {
      console.error("Submission error:", err);
      showFeedback(feedback, "Could not connect to server. Please call us directly at +91 9689820892.", "error");
    } finally {
      submitBtn.disabled = false;
      submitBtn.innerHTML = originalBtnText;
    }
  });
}

function showFeedback(el, text, type) {
  if (!el) return;
  el.classList.remove("hidden", "bg-green-50", "text-green-800", "border-green-200", "bg-red-50", "text-red-800", "border-red-200");
  
  if (type === "success") {
    el.classList.add("bg-green-50", "text-green-800", "border", "border-green-200");
  } else {
    el.classList.add("bg-red-50", "text-red-800", "border", "border-red-200");
  }
  el.innerHTML = text;
}
