class CalculadoraIpi:
    def __init__(self, valor_total: float, aliquota: float):
        # Conversão forçada para float para evitar erros caso venha texto por engano
        self.valor_total: float = float(valor_total)
        self.aliquota: float = float(aliquota)

    @property
    def fator(self) -> float:
        """Calcula o fator de divisão com base na alíquota do IPI."""
        return 1.0 + (self.aliquota / 100.0)

    @property
    def valor_sem_ipi(self) -> float:
        """Calcula o valor do material descontando o IPI."""
        if self.fator == 0:
            return 0.0
        return self.valor_total / self.fator

    @property
    def valor_imposto(self) -> float:
        """Calcula a parcela de imposto contida no valor total."""
        return self.valor_total - self.valor_sem_ipi

    def para_dicionario(self) -> dict:
        """
        Exporta os resultados em formato de dicionário para integração com a interface.
        """
        return {
            "total_com_ipi": self.valor_total,
            "ipi_porcentagem": self.aliquota,
            "total_sem_ipi": self.valor_sem_ipi,
            "ipi_valor": self.valor_imposto
        }

    def __str__(self) -> str:
        return (
            f"Valor total (Com IPI): R$ {self.valor_total:.2f}\n"
            f"Valor sem IPI:        R$ {self.valor_sem_ipi:.2f}\n"
            f"Valor do IPI:         R$ {self.valor_imposto:.2f}\n"
            f"Alíquota:             {self.aliquota:.2f} %"
        )


if __name__ == "__main__":
    calc = CalculadoraIpi(3520, 5.2)
    print(calc)
