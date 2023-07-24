const bthome = document.querySelector('.bt_home');
const wrapper = document.querySelector('.wrapper');
const contact = document.querySelector('.contact');
const about = document.querySelector('.about');
const service = document.querySelector('.service');


const loginLink = document.querySelector('.login-link');
const registerLink = document.querySelector('.register-link');
const btnPopupAbout = document.querySelector('.bt_login_Popup_about');
const btnPopup = document.querySelector('.bt_login_Popup');
const btnPopup1 = document.querySelector('.bt_login_Popup1');
const btnPopupService = document.querySelector('.bt_service_Popup');


const iconClose = document.querySelector('.icon-close');
const iconclosecontact =document.querySelector('.icon-close-contact'); 
const iconcloseabout =document.querySelector('.icon-close-about'); 
const iconcloseservice =document.querySelector('.icon-close-service'); 
registerLink.addEventListener('click',()=>{
    wrapper.classList.add('active');
});

loginLink.addEventListener('click',()=>{
    wrapper.classList.remove('active');
});

btnPopup.addEventListener('click',()=>{
    contact.classList.remove('contact_active');
    about.classList.remove('about_active');
    service.classList.remove('service_active');
    wrapper.classList.add('active-popup');
});
btnPopup1.addEventListener('click',()=>{
    wrapper.classList.remove('active-popup');
    about.classList.remove('about_active');
    service.classList.remove('service_active');
    contact.classList.add('contact_active');

});

btnPopupAbout.addEventListener('click',()=>{
    wrapper.classList.remove('active-popup');
    contact.classList.remove('contact_active');
    service.classList.remove('service_active');
    about.classList.add('about_active');

});
btnPopupService.addEventListener('click',()=>{
    wrapper.classList.remove('active-popup');
    contact.classList.remove('contact_active');
    about.classList.remove('about_active');
    service.classList.add('service_active');
});




iconClose.addEventListener('click',()=>{
    wrapper.classList.remove('active-popup');
});
iconclosecontact.addEventListener('click',()=>{
    contact.classList.remove('contact_active');
});
iconcloseabout.addEventListener('click',()=>{
    about.classList.remove('about_active');
    console.log('not work')
});
iconcloseservice.addEventListener('click',()=>{
    service.classList.remove('service_active');
});

bthome.addEventListener('click',()=>{
    wrapper.classList.remove('active-popup');
    contact.classList.remove('contact_active');
    about.classList.remove('about_active')
    service.classList.remove('service_active');
});



const next_page1 = document.querySelector('.next-pg1');
const next_page2 = document.querySelector('.next-pg2');
next_page1.addEventListener('click',()=>{
    service.classList.remove('service_active');
    wrapper.classList.add('active-popup');
});
next_page2.addEventListener('click',()=>{
    service.classList.remove('service_active');
    wrapper.classList.add('active-popup');
})