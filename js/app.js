// JavaScript to handle mouseover and mouseout events
var activeMethodPill = null;
var activeScenePill = null;
var activeModePill = null;
var activeVidID = 0;
var select = false;
var activeMethodPillDenoising = null;
var activeScenePillDenoising = null;
var activeModePillDenoising = null;
var activeVidIDDenoising = 0;


$(document).ready(function () {
    var editor = CodeMirror.fromTextArea(document.getElementById("bibtex"), {
        lineNumbers: false,
        lineWrapping: true,
        readOnly: true
    });
    $(function () {
        $('[data-toggle="tooltip"]').tooltip()
    });

    activeMethodPill = $('.method-pill').filter('.active')[0];
    activeModePill = $('.mode-pill').filter('.active')[0];
    activeScenePill = $('.scene-pill').filter('.active')[0];
    activeMethodPillDenoising = $('.method-pill-denoising').filter('.active')[0];
    activeModePillDenoising = $('.mode-pill-denoising').filter('.active')[0];
    activeScenePillDenoising = $('.scene-pill-denoising').filter('.active')[0];

    resizeAndPlay($('#sparsity')[0]);
});

function selectCompVideo(methodPill, scenePill, n_views, modePill) {
    // Your existing logic for video selection
    // var video = document.getElementById("compVideo");
    select = true;
    var videoSwitch = document.getElementById("compVideoSwitch");
    var viewNum = document.getElementById("compVideoValue");

    if (activeMethodPill) {
        activeMethodPill.classList.remove("active");
    }
    if (activeScenePill) {
        activeScenePill.classList.remove("active");
    }
    if (modePill) {
        activeModePill.classList.remove("active");
        modePill.classList.add("active");
        activeModePill = modePill;
    }
    activeMethodPill = methodPill;
    activeScenePill = scenePill;
    methodPill.classList.add("active");
    scenePill.classList.add("active");
    method = methodPill.getAttribute("data-value");
    pill = scenePill.getAttribute("data-value");
    mode = activeModePill.getAttribute("data-value");

    // if (videoSwitch.checked) {
    //     mode = 'depth'
    // } else {
    //     mode = 'rgb'
    // }

    // swap video to avoid flickering
    activeVidID = 1 - activeVidID;
    var video_active = document.getElementById("compare");
    // var video_active = document.getElementById("compVideo" + activeVidID);
    // var video_hidden = document.getElementById("compVideo" + (1 - activeVidID));
    video_active.src = "videos/" + mode + "_" + pill + "_" +method + "_vs_ours.mp4";
    video_active.load();

    if (n_views) {
        viewNum.innerHTML = n_views;
    }
}

function selectCompVideoDenoising(methodPillDenoising, scenePillDenoising, n_views, modePillDenoising) {
    // Your existing logic for video selection
    // var video = document.getElementById("compVideo");
    select = true;
    // var videoSwitch = document.getElementById("compVideoSwitch");
    var viewNum = document.getElementById("compVideoValue");

    if (activeMethodPillDenoising) {
        activeMethodPillDenoising.classList.remove("active");
    }
    if (activeScenePillDenoising) {
        activeScenePillDenoising.classList.remove("active");
    }
    if (modePillDenoising) {
        activeModePillDenoising.classList.remove("active");
        modePillDenoising.classList.add("active");
        activeModePillDenoising = modePillDenoising;
    }
    activeMethodPillDenoising = methodPillDenoising;
    activeScenePillDenoising = scenePillDenoising;
    methodPillDenoising.classList.add("active");
    scenePillDenoising.classList.add("active");
    method = methodPillDenoising.getAttribute("data-value");
    pill = scenePillDenoising.getAttribute("data-value");
    mode = activeModePillDenoising.getAttribute("data-value");

    // if (videoSwitch.checked) {
    //     mode = 'depth'
    // } else {
    //     mode = 'rgb'
    // }

    // swap video to avoid flickering
    activeVidIDDenoising = 1 - activeVidIDDenoising;
    var video_active = document.getElementById("compare_denoising");
    // var video_active = document.getElementById("compVideo" + activeVidID);
    // var video_hidden = document.getElementById("compVideo" + (1 - activeVidID));
    video_active.src = "videos/" + mode + "_" + pill + "_" +method + "_vs_ours.mp4";
    video_active.load();

    if (n_views) {
        viewNum.innerHTML = n_views;
    }
}