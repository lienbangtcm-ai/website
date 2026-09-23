(function(){
  function rewriteLegacyLinks(){
    var fixed={
      '/team/':'/team/',
      '/health-blog/':'/symptoms/',
      '/support/':'/#site-footer',
      '/profile/':'/team/#zhang-yu',
      '/tsai-ru-hui/':'/team/#tsai-ru-hui',
      '/zhang-you-ming/':'/team/#zhang-you-ming'
    };
    document.querySelectorAll('a[href]').forEach(function(a){
      var href=a.getAttribute('href');
      if(href==='/#doctor-team'){a.setAttribute('href','/team/');return;}
      if(!href || !/^https?:\/\/(?:www\.)?lienbangtcm\.tw\//i.test(href)) return;
      try{
        var u=new URL(href);
        var path=u.pathname || '/';
        var target=fixed[path] || path;
        if(!fixed[path]){
          if(u.search) target+=u.search;
          if(u.hash) target+=u.hash;
        }
        a.setAttribute('href',target);
      }catch(e){}
    });
  }

  function init(){
    rewriteLegacyLinks();
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