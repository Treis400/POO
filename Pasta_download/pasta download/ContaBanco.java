public class ContaBanco {
    
    public int numConta;
    protected String tipo; 
    private String dono;
    private float saldo;
    private boolean status;

    public ContaBanco() {
        this.saldo = 0;
        this.status = false;
    }

    public ContaBanco(int numConta, String tipo, String dono, float saldo, boolean status) {
        this.numConta = numConta;
        this.tipo = tipo;
        this.dono = dono;
        this.saldo = saldo;
        this.status = status;

    }

    public void estadoAtual () {
        System.out.println("_________________________");
        System.out.println("Conta " + this.getNumConta());
        System.out.println("Tipo " + this.getTipo());
        System.out.println("Dono " + this.getDono());
        System.out.println("Saldo R$ " + this.getSaldo());
        System.out.println("Status " + this.getStatus());
        System.out.println("_________________________");
    }

    public void abrirConta (String t) {
        this.setTipo(t);
        this.setStatus(true);

        if (t == "CC") {
            this.setSaldo (50);
        } else if (t == "CP") {
            this.setSaldo(150);
        }
        System.out.println("Conta Aberta com sucesso !! ");
        }


    public void fecharConta () {
        if (this.getSaldo() > 0) {
            System.out.println("A conta não pode ser fechada, pois há saldo positivo nela, saque o valor para que a operação seja concluida ! ");
        } else if (this.getSaldo() < 0) {
            System.out.println("A conta não pode ser fechada, pois há débito em aberto! ");
        } else {
            this.setStatus(false);
            System.out.println("Conta Fechada com Sucesso ! ");
        }
    }


    public void depositar (float v) {
        if (this.getStatus()) {
            this.setSaldo(this.getSaldo() + v);
            System.out.println("Valor depositado com sucesso ! " + this.getDono());
        } else {
            System.out.println("Impossivem depositar em uma conta fechada ");
        }

    }
    public void sacar (float v) {
        if (this.getStatus()) {
           if (this.getSaldo() >= v) {
                this.setSaldo(this.getSaldo() - v);
                System.out.println("Saque realizado com sucesso na conta de " + this.getDono());
           } else {
                System.out.println("Saldo insuficiente para saque!");
            };
        } else {
            System.out.println("Impossivel sacar de uma conta Inativa ");
        }

    }
    public void pagarMensal () {
        int v = 0;
        if (this.getTipo() == "CC") {
            v = 12;
        } else if (this.getTipo() == "CP"){
            v = 20;
        }
        if (this.getStatus()) {
            this.setSaldo(this.getSaldo() - v);
            System.out.println("Mensalidade paga com sucesso por " + this.getDono());
        } else {
            System.out.println("Impossivel pagar em um conta inativa");
        }

    }

    public int getNumConta() {
        return numConta;
    }
    public void setNumConta(int numConta) {
        this.numConta = numConta;
    }
    public String getTipo() {
        return tipo;
    }
    public void setTipo(String tipo) {
        this.tipo = tipo;
    }
    public String getDono() {
        return dono;
    }
    public void setDono(String dono) {
        this.dono = dono;
    }
    public float getSaldo() {
        return saldo;
    }
    public void setSaldo(float saldo) {
        this.saldo = saldo;
    }
    public boolean getStatus() {
        return status;
    }
    public void setStatus(boolean status) {
        this.status = status;
    }

    
}
