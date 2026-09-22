(function(){
  function init(){
    document.querySelectorAll('.global-header').forEach(function(header){
      if(header.dataset.mobileMenuReady==='1') return;
      header.dataset.mobileMenuReady='1';

      var nav=header.querySelector(':scope > nav');
      var brand=header.querySelector('.global-brand');
      if(!nav||!brand) return;

      var toggle=document.createElement('button');
      toggle.className='global-menu-toggle';
      toggle.type='button';
      toggle.setAttribute('aria-label','開啟網站選單');
      toggle.setAttribute('aria-expanded','false');
      toggle.innerHTML='<span></span><span></span><span></span>';
      header.insertBefore(toggle,brand);

      function closeMenu(){
        header.classList.remove('menu-open');
        document.body.classList.remove('global-menu-open');
        toggle.setAttribute('aria-expanded','false');
        toggle.setAttribute('aria-label','開啟網站選單');
      }
      function openMenu(){
        header.classList.add('menu-open');
        document.body.classList.add('global-menu-open');
        toggle.setAttribute('aria-expanded','true');
        toggle.setAttribute('aria-label','關閉網站選單');
      }

      toggle.addEventListener('click',function(e){
        e.stopPropagation();
        header.classList.contains('menu-open') ? closeMenu() : openMenu();
      });

      nav.addEventListener('click',function(e){
        if(e.target.closest('a')) closeMenu();
      });

      document.addEventListener('click',function(e){
        if(header.classList.contains('menu-open') && !nav.contains(e.target) && !toggle.contains(e.target)){
          closeMenu();
        }
      });

      document.addEventListener('keydown',function(e){
        if(e.key==='Escape') closeMenu();
      });

      window.addEventListener('resize',function(){
        if(window.innerWidth>820) closeMenu();
      });
    });
  }

  if(document.readyState==='loading') document.addEventListener('DOMContentLoaded',init);
  else init();
})();