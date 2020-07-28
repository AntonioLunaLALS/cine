function confirmarEliminacion(id){
    Swal.fire({
        title: 'Seguro que quiere Elimiar la Pelicula',
        text: "No podras deshacer esta Accion",
        icon: 'warning',
        showCancelButton: true,
        confirmButtonColor: '#3085d6',
        cancelButtonColor: '#d33',
        confirmButtonText: 'Si, Eliminar!',
        cancelButtonText: 'Cancelar'
      }).then((result) => {
          if(result.value){
              window.location.href = "/eliminar_pelicula/"+id+"/";
          }
   
      })
}