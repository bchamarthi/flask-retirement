document.getElementById('falu').onclick = partyFalu
document.getElementById('smaragdine').onclick = partySmaragdine
document.getElementById('glaucous').onclick = partyGlaucous
document.getElementById('sarcoline').onclick = partySarcoline

function partyFalu() {
  document.querySelector('.st2').style.fill = 'rgb(126,37,30)'
  document.querySelector('.st3').style.fill = 'rgb(63,19,15)'
  document.querySelector('.st7').style.fill = 'rgb(126,37,30)'
  document.querySelector('.st4').style.fill = 'rgb(63,19,15)'
}

function partySmaragdine() {
  document.querySelector('.st2').style.fill = 'rgb(25,145,113)'
  document.querySelector('.st3').style.fill = 'rgb(13,73,67)'
  document.querySelector('.st7').style.fill = 'rgb(25,145,113)'
  document.querySelector('.st4').style.fill = 'rgb(13,73,67)'
}

function partyGlaucous() {
  document.querySelector('.st2').style.fill = 'rgb(96,126,175)'
  document.querySelector('.st3').style.fill = 'rgb(48,63,88)'
  document.querySelector('.st7').style.fill = 'rgb(96,126,175)'
  document.querySelector('.st4').style.fill = 'rgb(48,63,88)'
}

function partySarcoline() {
  document.querySelector('.st2').style.fill = 'rgb(250,218,170)'
  document.querySelector('.st3').style.fill = 'rgb(125,109,85)'
  document.querySelector('.st7').style.fill = 'rgb(250,218,170)'
  document.querySelector('.st4').style.fill = 'rgb(125,109,85)'
}