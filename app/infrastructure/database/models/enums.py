from enum import Enum

class StatusOrders(str, Enum):
    AGUARDANDO_PAGAMENTO = "AGUARDANDO_PAGAMENTO"
    EM_PREPARACAO = "EM_PREPARACAO"
    EM_ROTA_ENTREGA = "EM_ROTA_ENTREGA"
    PEDIDO_ENTREGUE = "PEDIDO_ENTREGUE"

class SourceOrders(str, Enum):
    APP = "APP"
    ATENDENTE = "ATENDENTE"
    TOTEM = "TOTEM"
    SITE = "SITE"

class PositionEmploy(str, Enum):
    ATENDENTE = "ATENDENTE"
    GERENTE = "GERENTE"
    FINANCEIRO = "FINANCEIRO"
    COZINHEIRO = "COZINHEIRO"
