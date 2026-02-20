function toggleMenu() {
    const menu = document.querySelector('.menu');
    const navMobile = document.querySelector('.nav-mobile');

    menu.classList.toggle('active');
    navMobile.classList.toggle('active');
} 

// change background videos
function changeVideo(name) {
    const bgVideoList = document.querySelectorAll('.bg-video');
    const videoContainer = document.querySelectorAll('.video-container');

    bgVideoList.forEach(video => {
        video.classList.remove('active');
        if (video.classList.contains(name)) {
            video.classList.add('active');
        }
    });

    videoContainer.forEach(video => {
        video.classList.remove('active');
        if (video.classList.contains(name)) {
            video.classList.add('active');
        }
    });
}