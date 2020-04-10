import cliente, cliente_repository

repo = cliente_repository.ClienteRepository()
repo.listar_clientes()

cli = cliente.Cliente('JOSÉ DA SILVA', 49)

repo.inserir_cliente(cli)
repo.listar_clientes()

repo.editar_cliente(1, cli)
repo.listar_clientes()

repo.remover_cliente(1)
repo.listar_clientes()
