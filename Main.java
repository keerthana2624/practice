
public class Main {
  public static void main(String[] args) {
    
        Test t = new Test();
        double a = t.power(3, 2);
        System.out.println(a);
      
      
        Test test = new Test();
        int result = test.division(6, 3);
        System.out.println(result);

  
        test.add(2,6);
        test.add(4,3);

    
        t.sub(2,3);
        System.out.println(t);


        Test med = new Test();
        System.out.println(med.evenOrNot(5));

        Test obj= new Test();
        int x =obj.pro(2, 5);
        System.out.println(x);

}
}
