function getSelectionText() {
    var text = "fa";
    var activeEl = document.activeElement;
    var activeElTagName = activeEl ? activeEl.tagName.toLowerCase() : null;
    console.log(activeEl.name)

    if (
      (activeElTagName == "textarea") || (activeElTagName == "input" &&
      /^(?:text|search|password|tel|url)$/i.test(activeEl.type)) &&
      (typeof activeEl.selectionStart == "number")
    ) {
        text = activeEl.value.slice(activeEl.selectionStart, activeEl.selectionEnd);
    } else if (window.getSelection) {
        console.log(window.getSelection().toString());
        text = window.getSelection().toString();
    }

    console.log("you selcted this ", text);
    return text;
}

document.onmouseup = document.onkeyup = document.onselectionchange = function() {
  getSelectionText();
};