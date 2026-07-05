document.addEventListener("DOMContentLoaded", function () {

const dob = document.querySelector('input[name="dob"]');

if (dob) {

dob.max = new Date().toISOString().split("T")[0];

}

});

document.querySelectorAll(".delete-btn").forEach(button => {

    button.addEventListener("click", function () {

        const id = this.dataset.id;

        document.getElementById("confirmDeleteBtn").href = "/delete/" + id;

    });

});