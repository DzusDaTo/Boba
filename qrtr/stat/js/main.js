const meta = `http://127.0.0.1:8000`
let genBtns = document.querySelectorAll('.video-qr-gen')

const genQ = (element, str) => {
    new QRCode(element, {
        text: str,
        colorDark : "#000000", 
        colorLight : "#ffffff",
        correctLevel : QRCode.CorrectLevel.H
    })
}

genBtns.forEach(element => {
    element.addEventListener('click', (event) => {
        if (event.target.closest('.video-container').querySelector('.video-generic')) {
            event.target.closest('.video-container').querySelector('.video-generic').remove()
            
            event.target.closest('.video-qr-gen').querySelector('.svg-play').style.transform = 'rotate(0deg)'
        } else {
            let shadowDiv = document.createElement("div")
            shadowDiv.classList.add(`video-generic`) 
            event.target.closest('.video-container').appendChild(shadowDiv)
            let currentId = event.target.closest('.video-container').getAttribute('data-id')
            let currentElement = event.target.closest('.video-container').querySelector('.video-generic')
            genQ(currentElement, `${meta}${currentId}`)
            event.target.closest('.video-container').querySelector('.video-generic').style.opacity = 1
            event.target.closest('.video-qr-gen').querySelector('.svg-play').style.transform = 'rotate(180deg)'
        }
    })
})