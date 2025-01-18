require_relative 'JobOffer'

class InfoJobOffer < JobOffer
  attr_accessor :salario, :modalidad, :jornada, :experiencia, :idioma

  def initialize(nombre, ubicacion, url, tipo_contrato, descripcion = "None")
    super(nombre, ubicacion, url, descripcion) # Llama al constructor de JobOffer
    @tipo_contrato = tipo_contrato
  end

  def save
    puts "Guardando : #{@nombre} con contrato #{@tipo_contrato}"
  end
end
