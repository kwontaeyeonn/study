// script.js
const videos = [
    {
        title: "Amazing Nature",
        thumbnail: "https://i.ytimg.com/vi/6lt2JfJdGSY/hqdefault.jpg",
        id: "6lt2JfJdGSY"
    },
    {
        title: "JavaScript Tutorial",
        thumbnail: "https://i.ytimg.com/vi/PkZNo7MFNFg/hqdefault.jpg",
        id: "PkZNo7MFNFg"
    }
];

const videoList = document.getElementById("video-list");

function renderVideos(videoArray) {
    videoList.innerHTML = '';
    videoArray.forEach(video => {
        const videoEl = document.createElement("div");
        videoEl.className = "video-card";
        videoEl.innerHTML = `
        <img src="${video.thumbnail}" alt="${video.title}">
        <div class="video-info">
            <h4>${video.title}</h4>
            <a href="https://www.youtube.com/watch?v=${video.id}" target="_blank">Watch</a>
        </div>
        `;
        videoList.appendChild(videoEl);
    });
}

renderVideos(videos);

document.getElementById("search-input").addEventListener("input", (e) => {
    const keyword = e.target.value.toLowerCase();
    const filtered = videos.filter(video =>
    video.title.toLowerCase().includes(keyword)
    );
    renderVideos(filtered);
});
