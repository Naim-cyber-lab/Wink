
const buttonAddLike = document.querySelectorAll('#likeEvent')

buttonAddLike.forEach(unLike => unLike.addEventListener('click',function(e){

  $.ajax({

    type:'POST',
    url:'/profil/DisplayEvents/', //on met l'url pour identifier à quel endroit à quel route (et donc quel vue) on va envoyer ce formulaire
    
    //On construie le dictionnaire qu'on va envoyer à la vue
    data: {
      'csrfmiddlewaretoken':$('input[name=csrfmiddlewaretoken]').val(),
      event_id:parseInt($(this).attr('identificationEvent') , 10),
      formAddLike: 1 ,
    },
    success: function(response) {
 
      console.log('successLike', response)
     
    }
  
  })
}));

const buttonAddLove = document.querySelectorAll('#LoveEvent')

buttonAddLove.forEach(unLike => unLike.addEventListener('click',function(e){

  $.ajax({

    type:'POST',
    url:'/profil/DisplayEvents/', //on met l'url pour identifier à quel endroit à quel route (et donc quel vue) on va envoyer ce formulaire
    
    //On construie le dictionnaire qu'on va envoyer à la vue
    data: {
      'csrfmiddlewaretoken':$('input[name=csrfmiddlewaretoken]').val(),
      event_id:parseInt($(this).attr('identificationEvent') , 10),
      formAddLove: 1 ,
    },
    success: function(response) {
      console.log('success', response)
    }
  
  })

}));
  const buttonAddSad = document.querySelectorAll('#SadEvent')

buttonAddSad.forEach(unLike => unLike.addEventListener('click',function(e){

  $.ajax({

    type:'POST',
    url:'/profil/DisplayEvents/', //on met l'url pour identifier à quel endroit à quel route (et donc quel vue) on va envoyer ce formulaire
    
    //On construie le dictionnaire qu'on va envoyer à la vue
    data: {
      'csrfmiddlewaretoken':$('input[name=csrfmiddlewaretoken]').val(),
      event_id:parseInt($(this).attr('identificationEvent') , 10),
      formAddSad: 1 ,
    },
    success: function(response) {
      console.log('success', response)
    }
  
  })
}));

  const buttonAddHaha = document.querySelectorAll('#HahaEvent')

buttonAddHaha.forEach(unLike => unLike.addEventListener('click',function(e){
  $.ajax({

    type:'POST',
    url:'/profil/DisplayEvents/', //on met l'url pour identifier à quel endroit à quel route (et donc quel vue) on va envoyer ce formulaire
    
    //On construie le dictionnaire qu'on va envoyer à la vue
    data: {
      'csrfmiddlewaretoken':$('input[name=csrfmiddlewaretoken]').val(),
      event_id:parseInt($(this).attr('identificationEvent') , 10),
      formAddHaha: 1 ,
    },
    success: function(response) {
      console.log('success', response)
    }
  
  })

}));

const buttonAddWow = document.querySelectorAll('#WowEvent')

buttonAddWow.forEach(unLike => unLike.addEventListener('click',function(e){

  $.ajax({

    type:'POST',
    url:'/profil/DisplayEvents/', //on met l'url pour identifier à quel endroit à quel route (et donc quel vue) on va envoyer ce formulaire
    
    //On construie le dictionnaire qu'on va envoyer à la vue
    data: {
      'csrfmiddlewaretoken':$('input[name=csrfmiddlewaretoken]').val(),
      event_id:parseInt($(this).attr('identificationEvent') , 10),
      formAddWow: 1 ,
    },
    success: function(response) {
      console.log('success', response)
    }
  
  })
}));

const buttonAddAngry = document.querySelectorAll('#AngryEvent')

buttonAddAngry.forEach(unLike => unLike.addEventListener('click',function(e){

  $.ajax({

    type:'POST',
    url:'/profil/DisplayEvents/', //on met l'url pour identifier à quel endroit à quel route (et donc quel vue) on va envoyer ce formulaire
    
    //On construie le dictionnaire qu'on va envoyer à la vue
    data: {
      'csrfmiddlewaretoken':$('input[name=csrfmiddlewaretoken]').val(),
      event_id:parseInt($(this).attr('identificationEvent') , 10),
      formAddAngry: 1 ,
    },
    success: function(response) {
      console.log('successAngry', response)
    }
  
  })
}));


const buttonDemandeParticipation = document.querySelectorAll('.demandeParticipation')

buttonDemandeParticipation.forEach(uneDemande => uneDemande.addEventListener('click',function(e){
$.ajax({

  type:'POST',
  url:'/profil/DisplayEvents/', //on met l'url pour identifier à quel endroit à quel route (et donc quel vue) on va envoyer ce formulaire
  
  //On construie le dictionnaire qu'on va envoyer à la vue
  data: {
    'csrfmiddlewaretoken':$('input[name=csrfmiddlewaretoken]').val(),
    event_id:parseInt($(this).attr('identificationEvent') , 10),
    formDemandeParticipation: 1 ,
  },
  success: function(response) {
    uneDemande.style.backgroundColor = "green";
    uneDemande.innerHTML = 'Demande faite !'
  }

})
}));