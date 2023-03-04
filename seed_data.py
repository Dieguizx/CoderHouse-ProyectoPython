from SocialTravel.models import Post

for _ in range(0,40):
    Post(carousel_caption_title="Carousel Titulo", 
    carousel_caption_description="Carousel Descripcion",
    heading="Viaje encabezado",
    description="Viaje descripcion"
    ).save()



