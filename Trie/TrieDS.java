import java.util.*;

class Trie{
  Trie arr[]=new Trie[26];
  boolean isEnd=false;
    public static void insert(Trie root,String s){
        Trie t=root;
        for(int i=0;i<s.length();i++){
          t.arr[s.charAt(i)-'a']=new Trie();
          t=t.arr[s.charAt(i)-'a'];
        }
        t.isEnd=true;
    }
    public static boolean search(Trie root,String s){
        Trie t=root;
        boolean flag=true;
        for(int i=0;i<s.length();i++){
            if(t.arr[s.charAt(i)-'a']==null){
                flag=false;
            }
            else{
                t=t.arr[s.charAt(i)-'a'];
                if(i==s.length()-1){
                if(t.isEnd==true){
                    return true;
                }else{
                    return false;
                }
            }
            }
        }
        return flag;
    }
    public static boolean prefix(Trie root,String s){
        Trie t=root;
        boolean flag=true;
        for(int i=0;i<s.length();i++){
            if(t.arr[s.charAt(i)-'a']==null){
                flag=false;
            }
            else{
                t=t.arr[s.charAt(i)-'a'];
            }
        }
        return flag;
    }
}

public class TrieDS {
    public static void main(String[] args) {
        Trie root=new Trie();
        String cities[] = {"shimla","safari","jammu","delhi","jammu","dehradun","jammu"};
        HashMap<String,Integer> map=new HashMap<String,Integer>();
        
        for(int i=0;i<cities.length;i++){
            map.put(cities[i],1);
        }
        for(int i=0;i<cities.length;i++){
            boolean flag=false;
            for(int j=1;j<cities[i].length() && flag==false;j++){
                if(Trie.prefix(root,cities[i].substring(0,j))==false){
                    System.out.println(cities[i].substring(0,j));
                    flag=true;
                }
            }
            if(flag==false){
                System.out.println(cities[i]+" "+map.get(cities[i]));  
            }
            Trie.insert(root,cities[i]);
            map.replace(cities[i],map.get(cities[i])+1);
        }
    }
    
    
}