var AdminPanel = document.getElementById("ADMIN_PANEL")
var Updateinfo = document.getElementById("UPDATE")

var visibility_ADMIN_PANEL = document.getElementById("ADMIN_PANEL_ALL")
var visibility_ADMIN_UPDATE = document.getElementById("ADMIN_UPDATE_ALL")


function ChangeSkill(number) {
    if (number == 1) {
        AdminPanel.className = "nav-link active"
        Updateinfo.className = "nav-link"

        visibility_ADMIN_PANEL.style = "display: block;"
        visibility_ADMIN_UPDATE.style = "display: none;"

    } else if (number == 2) {
        AdminPanel.className = "nav-link"
        Updateinfo.className = "nav-link active"

        visibility_ADMIN_PANEL.style = "display: none;"
        visibility_ADMIN_UPDATE.style = "display: block;"
    }
}



function ellipsis_box(elemento, max_chars) {
    limite_text = $(elemento).text();
    if (limite_text.length > max_chars) {
        limite = limite_text.substr(0, max_chars) + " ...";
        $(elemento).text(limite);
    }
}
$(function() {
    ellipsis_box(".limitado-info", 240);
});