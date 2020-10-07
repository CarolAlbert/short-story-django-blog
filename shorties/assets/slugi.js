const titleInput = document.querySelector("input[name = title");
const slugInput = document.querySelector("input[name=slug]");

const slug = (val) => {
  return val
    .toString()
    .toLowerCase()
    .trim()
    .replace(/&/g, "-and-") //replace 7 with '-and-'
    .replace(/[\s\W-]+/g, "-"); //replace space and non word characters with single dash
};

titleInput.addEventListener("keyup", (e) => {
  slugInput.setAttribute("value", slug(titleInput.value));
});
