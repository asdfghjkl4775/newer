const signUpBtn = document.getElementById("signUp");
const signInBtn = document.getElementById("signIn");
const container2 = document.querySelector(".container2");

signUpBtn.addEventListener("click", () => {
  container2.classList.add("right-panel-active");
});
signInBtn.addEventListener("click", () => {
  container2.classList.remove("right-panel-active");
});