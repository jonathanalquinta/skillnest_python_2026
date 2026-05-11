class SuscripcionStreaming:
    costos_suscripcion = {"Gratis": 0,"Estándar": 5.99,"Premium": 10.99}

    def __init__(self, usuario, tipo_suscripcion="Gratis"):
        self.usuario = usuario
        self.tipo_suscripcion = tipo_suscripcion
        self.costo_mensual = self.costos_suscripcion(tipo_suscripcion)
        self.saldo_pendiente = self.costo_mensual

    def realizar_pago(self, monto): 
        """Reduce el saldo pendiente según el monto pagado."""
        reducir_monto = min(monto, self.saldo_pendiente)
        self.saldo_pendiente -= reducir_monto

    def cambiar_suscripcion(self, nuevo_tipo):
        """Cambia el tipo de suscripción y actualiza el costo mensual."""
        if nuevo_tipo in self.costos_suscripcion:
            self.tipo_suscripcion = nuevo_tipo
            self.saldo_pendiente = self.costos_suscripcion[nuevo_tipo]

    def ver_contenido_exclusivo(self):
        """Permite ver contenido exclusivo según el tipo de suscripción."""

        if self.tipo_suscripcion == "Gratis":
            return "No tienes acceso a contenido exclusivo."

        elif self.tipo_suscripcion == "Estándar":
            return "Acceso a contenido exclusivo estándar."

        elif self.tipo_suscripcion == "Premium":
            return "Acceso a todo el contenido exclusivo."
       

    def mostrar_info_suscripcion(self):
       """Muestra la información de la suscripción del usuario."""
       pass


benjamin = SuscripcionStreaming("estandar")
alexander = SuscripcionStreaming("premium")
juan = SuscripcionStreaming("gratis")