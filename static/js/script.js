/* ==========================================
   DAR AL OUD
   script.js
========================================== */

"use strict";

/* Page Loaded */
document.addEventListener("DOMContentLoaded", function () {
    console.log("Dar Al Oud Loaded Successfully");
});


/* Confirm Remove From Cart */
document.querySelectorAll(".btn-danger").forEach(function (button) {

    button.addEventListener("click", function (e) {

        if (!confirm("Are you sure you want to remove this item?")) {

            e.preventDefault();

        }

    });

});


/* Scroll To Top Button */

const topButton = document.createElement("button");

topButton.innerHTML = "↑";

topButton.id = "topButton";

document.body.appendChild(topButton);

topButton.style.position = "fixed";
topButton.style.bottom = "20px";
topButton.style.right = "20px";
topButton.style.display = "none";
topButton.style.width = "50px";
topButton.style.height = "50px";
topButton.style.border = "none";
topButton.style.borderRadius = "50%";
topButton.style.background = "#d4af37";
topButton.style.color = "#000";
topButton.style.fontSize = "22px";
topButton.style.cursor = "pointer";
topButton.style.zIndex = "9999";

window.addEventListener("scroll", function () {

    if (window.scrollY > 300) {

        topButton.style.display = "block";

    } else {

        topButton.style.display = "none";

    }

});

topButton.addEventListener("click", function () {

    window.scrollTo({

        top: 0,

        behavior: "smooth"

    });

});


/* Current Year */

const year = document.getElementById("year");

if (year) {

    year.innerHTML = new Date().getFullYear();

}