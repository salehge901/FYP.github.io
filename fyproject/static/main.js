
const eventBox =document.getElementById("event-box")
const countdownBox = document.getElementById("countdown-box")
const eventDate = Date.parse(eventBox.textContent)
setInterval(()=>{
const now = new Date("Jan 5, 2022 15:37:25").getTime()
const diff = eventDate - now
const d = Math.floor(eventDate / (1000 * 60 * 60 *24)-(now / 1000 * 60 * 60 *24))
const g =  Math.floor((eventDate / (1000 * 60 * 60 )-(now / 1000 * 60 * 60 ))%24)
const i =  Math.floor((eventDate / (1000 * 60  )-(now / 1000 * 60 )) % 60)
const s =  Math.floor((eventDate / (1000)-(now / 1000)) % 60)
if(diff>0)
{
  countdownBox.innerHtml = d +"days," + g + "Horse" + i + "minuite" + s + "second"
}
 else{
}

},1000)