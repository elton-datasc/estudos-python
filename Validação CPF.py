
cpf = "168.995.350-09"
n = cpf.split(".")
cpf_novo = (n[0] + n[1] + n[2][:3])
print(cpf_novo)

