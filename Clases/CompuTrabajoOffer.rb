require_relative 'JobOffer'

class CompuTrabajoOffer < JobOffer
  attr_accessor :conocimientos, :modalidad,  :experiencia, :idioma, :salario

  def initialize(nombre, ubicacion,url, modalidad="None" ,conocimientos="None" , experiencia = "None", idioma = "None",  descripcion = "None", salario="None")
    super(nombre, ubicacion, salario,modalidad,url, descripcion)
    @conocimientos = conocimientos
    
    @experiencia = experiencia
    @idioma = idioma      
  end
  def setModalidad(modal)
    @modalidad = modal
  end
  def setConocimientos(conocimientos)
    @conocimientos = conocimientos
  end

  def setExperiencia(exp)
    @experiencia = exp
  end
  def setIdioma (idiom)
    @idioma = idiom
  end

  def hash
    @nombre.hash
  end
  def save(filecsv)
    puts "Guardando oferta de CompuTrabajo #{@nombre}"
    CSV.open(filecsv, 'a') do |csv|
      csv << [@nombre, @ubicacion,  @salario, @modalidad, @idioma, @experiencia,@conocimientos, @url,@descripcion]
    end
  end
end
