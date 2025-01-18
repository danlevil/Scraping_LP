require_relative 'JobOffer'

class EmpleoOffer < JobOffer  
  attr_accessor :salario, :habilidades_Clave , :formacion , :experiencia

  def initialize(nombre, ubicacion, url, salario, modalidad="None", habilidades_Clave = "None", formacion= "None", experiencia = "None", descripcion="None")
    
    super(nombre, ubicacion, url,salario, modalidad, descripcion) 
    @habilidades_Clave = habilidades_Clave
    @formacion = formacion
    @experiencia = experiencia
  end

  def save(filecsv)
    puts "Guardando oferta de Empleo.com: #{@nombre}"
    CSV.open(filecsv, 'a') do |csv|
      csv << [@nombre, @ubicacion, @salario, @habilidades_Clave, @formacion, @experiencia, @modalidad,@url,@descripcion]
    end
  end
  def setHabilidades(habilidades)
        @habilidades_Clave = habilidades
  end
  def setFormacion(formacion)
        @formacion = formacion
  end
  def setExperiencia(exp)
        @experiencia = exp
  end
  def setDescripcion(descripcion)
    @descripcion = descripcion
  end
  def hash
    @nombre.hash
  end


end
