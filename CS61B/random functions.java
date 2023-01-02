testing

    public static boolean allPairsCheck(BinaryPredicate p, IntList L){    
        if (L.size() == 0 || L.size == 1){
            return true;
        }

        for (int i = 0; i < N, i++){ // can't actually iterate like this
            if (!p(L[i], L[i+1])){
                return false;
            }
        }

        return true;
    }


    public static boolean allPairsCheck(BinaryPredicate p, IntList L){

        for (int i = L, (i == null) && !(i.tail == null)); i = i.tail){
            if (!p.test(i.head, i.tail.head)){
                return false;
            }
        }  

        return true;
        
        
    }

    public class Utils {
        return allPairsCheck(new ascending, L)
    }

    class ascending implements BinaryPredicate{
        public boolean test(int a, int b){
            return b > a;
        }
    }


public class Shove{
    /*
        If you want to do this recursively, all we have to do is add a recursive call in here and set the endpoint to when the final list isn't changed at all. So save the final list to output and then compare AssertTrue(A, arraycopy);
    */
    static void MoveOver(int[] A){

        int compare = A[A.length-1];
        
        int N = A.length;
        while (N > 1){
            if (A[N] < compare){
                for (int i = N, i < A.length-1; i++){
                    A[i] = temp;
                    A[i+1] = A[i];
                    A[i+1] = temp; // rotates everything over by one, this is basically bubble sort.
                }
            }
        }
    }
}