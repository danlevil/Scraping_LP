class JobOffer
    attr_accessor :nombre, :ubicacion, :url, :salario , :modalidad ,:descripcion
  
    def initialize(nombre, ubicacion, url, salario ="None" , modalidad = "None", descripcion = "None")
      @nombre = nombre
      @ubicacion = ubicacion
      @modalidad = modalidad
      @url = url
      @salario = salario
      @descripcion = descripcion
    end
  
    def save
      puts "Guardando oferta de trabajo genérica."
    end
  
    def setDescripcion(descripcion)
      @descripcion = descripcion
    end
  
  end
  