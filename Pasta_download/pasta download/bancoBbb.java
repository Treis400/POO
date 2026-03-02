public class bancoBbb {
    public static void main(String[] args)  {
        
        System.out.println("Bem vindo ao Banco Bbb ");
        ContaBanco p1 = new ContaBanco();
        p1.setNumConta(0001);
        p1.setDono("Thiago Reis ");
        p1.abrirConta("CC");
        p1.depositar(300);
        p1.sacar(150);

        ContaBanco p2 = new ContaBanco();
        p2.setNumConta(0002);
        p2.setDono("Damaris Salete");
        p2.abrirConta("CP");
        p2.depositar(500);
        p2.sacar(180);
        



        p1.estadoAtual();
        p2.estadoAtual();


        
    }
}