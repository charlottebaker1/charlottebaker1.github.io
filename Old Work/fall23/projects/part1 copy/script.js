// script.js
const menuToggle = document.querySelector('.menu-toggle');
const navLinks = document.querySelector('.nav-links');

menuToggle.addEventListener('click', () => {
  navLinks.classList.toggle('menu-open');
});

const panelButtons = document.querySelectorAll('.panel-heading');

panelButtons.forEach((button) => {
  button.addEventListener('click', () => {
    const panel = button.nextElementSibling;
    panel.style.display = panel.style.display === 'block' ? 'none' : 'block';
  });
});
const contactForm = document.getElementById('contact-form');
const successMessage = document.getElementById('success-message');
const errorMessage = document.getElementById('error-message');

contactForm.addEventListener('submit', async (e) => {
  e.preventDefault();
  // Add code here to send the form data via email (server-side).
  // Display success or error messages accordingly.
});
// script.js
fetch('data.json')
  .then((response) => response.json())
  .then((data) => {
    const dataDisplay = document.getElementById('data-display');
    data.forEach((item) => {
      const card = document.createElement('div');
      card.innerHTML = `
        <h3>${item.title}</h3>
        <p>${item.description}</p>
        <img src="${item.image}" alt="${item.title}">
      `;
      dataDisplay.appendChild(card);
    });
  });
// script.js (common to all pages)
const navLinks = document.querySelectorAll('.nav-links a');
const currentURL = window.location.href;

navLinks.forEach((link) => {
  if (currentURL === link.href) {
    link.classList.add('active');
  }
});
