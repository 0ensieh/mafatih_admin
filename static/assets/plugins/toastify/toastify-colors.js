const purple = "rgb(108,95,252)";
const red = "rgb(243,75,75)";


function showToast(text, background_color) {
  Toastify({
    text: text,
    duration: 3000,
    newWindow: true,
    close: true,
    gravity: "top", // `top` or `bottom`
    position: "center", // `left`, `center` or `right`
    stopOnFocus: true, // Prevents dismissing of toast on hover
    style: {
      background: background_color
    },
    onClick: function () {
    } // Callback after click
  }).showToast();
}
