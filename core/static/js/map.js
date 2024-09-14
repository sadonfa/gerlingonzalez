document.addEventListener("DOMContentLoaded", (event) =>{

    setTimeout(() => {
      document.querySelector("#load-iframe-map").innerHTML = `
   <iframe
                  class="contact__iframe"
                  frameborder="0"
                  scrolling="no"
                  marginheight="0"
                  marginwidth="0"
                  loading="lazy"
                  referrerpolicy="no-referrer-when-downgrade"
                  src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d31401.084480936413!2d-75.43545766912833!3d10.331034796663568!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x8ef620e02fa9013f%3A0x1f09c5899b5832bc!2sTurbaco%2C%20Bol%C3%ADvar!5e0!3m2!1ses!2sco!4v1724946425304!5m2!1ses!2sco"
                ></iframe>
   `;  
    }, 500);
   
})