var container = document.querySelector('.container');
var preGroup = document.querySelector('.preGroup');
var nounalizerGroup = document.querySelector('.nounalizerGroup');
var postGroup = document.querySelector('.postGroup');
var nullObject = document.querySelector('.null-object');
var pageNullObject = document.querySelector('.page-null-object');
var preMask = document.querySelector('.preMask');
var lightBlink = document.querySelector('.lightBlink');
var link = document.querySelector('.link');

var bendLeftAmount = 0;
var bendRightAmount = 0;

TweenMax.set([container,'#nounalizer'], {
  position: 'absolute',
  top: '50%',
  left: '50%',
  xPercent: -50,
  yPercent: -50
});

//blink the light
var blinkTween = TweenMax.to(lightBlink, 0.3, {
  fill: '#76C043',
  repeat: -1,
  ease: SteppedEase.config(1),
  yoyo: true,
  paused:true
})

var pageDragger = Draggable.create(pageNullObject, {
  trigger:preGroup,
  type:'y',
  onDrag:onPageDrag
})

var tl = new TimelineMax({
  onComplete:resetShredder,
  paused:true,
  immediateRender:true
});

tl.set('.post', {
    y: 40 // how far back to 300art the processed page
  })
  .to(preMask, 1, {
    y: -300, // where to end the page to be processed
    ease: Power1.easeInOut
  })

  .to(preGroup, 1, {
    y: 300,
    ease: Power1.easeInOut
  }, '-=1')

  .to('.post', 0.5, {
    y: 320,
    ease: Power1.easeOut
  }, '-=0.5')

  .to(nullObject, 0.8, {
      ease: SlowMo.ease.config(0.1, 0.8, false)
    }, '-=0.3')

.staggerTo('.post', 0.6, {
  rotation: 0,
  y: 640,
  ease: Power4.easeIn
}, 0, '-=0.5')




function onPageDrag(e){

  var posY = pageNullObject._gsTransform.y;
  TweenMax.set(preMask, {
    y:-posY
  })

  TweenMax.set(preGroup, {
      y:posY
    })

  if(posY >=50){
    pageDragger[0].disable();
    tl.play();
    blinkTween.play();
  }
}

function resetShredder(){
  blinkTween.time(0);
  blinkTween.pause();
  tl.seek(0);
  tl.pause();
  TweenMax.set([preMask,preGroup, pageNullObject], {
    y:0,
    alpha:0
  })
  TweenMax.set('.post',{
    y:-300
  })

  pageDragger[0].enable();


  TweenMax.to(preGroup, 0.6, {
    alpha:1,
    ease:Power3.easeIn
  })
}

TweenMax.to('.info', 0.9, {
  alpha:0.5,
  repeat:-1,
  yoyo:true,
  ease:Power1.easeIn
})

resetShredder();
