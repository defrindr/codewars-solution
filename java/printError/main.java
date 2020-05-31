
class PrinterTest {
    public static void main(String args[]) {
        System.out.println("printerError Fixed Tests");
        String s="aaaaaaaaaaaaaaaabbbbbbbbbbbbbbbbbbmmmmmmmmmmmmmmmmmmmxyz";
        System.out.println(printerError(s));
    }
    public static String printerError(String s) {
        int resultError = 0;
        for (int i=0;i<s.length();i++) if((int)s.charAt(i)<97 || (int)s.charAt(i)>109) resultError ++;
        return resultError+"/"+s.length();
    }
}