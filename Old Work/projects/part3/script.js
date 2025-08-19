function toggleMenu() {
    const navLinks = document.querySelector('.nav-links');
    navLinks.classList.toggle('show');
  }
  
  function jumpToAssignments() {
    window.location.href = "school.html";
  }
  // Add these functions to script.js

document.addEventListener("DOMContentLoaded", function () {
    updateMonth();
    highlightCurrentWeek();
  });
  
  function updateMonth() {
    const currentDate = new Date();
    const monthName = currentDate.toLocaleString("default", { month: "long" });
    document.getElementById("month-title").textContent = `${monthName} ${currentDate.getFullYear()}`;
  }
  
  function highlightCurrentWeek() {
    const currentDate = new Date();
    const currentWeek = currentDate.getDate() / 7;
    const weekElements = document.querySelectorAll(".week");
    
    weekElements.forEach((week, index) => {
      if (index === Math.floor(currentWeek)) {
        week.classList.add("current-week");
      }
    });
  }
  