package gitlet;

import java.util.ArrayList;
import java.util.TreeMap;
import java.io.Serializable;
import java.util.Collection;
public class Tree implements Serializable {

    /** The current commit.*/
    private Commit _current;
    /** The commit history.*/
    private TreeMap<String, Commit> _history;
    /** An arraylist of commits, which can be sorted using a comparator.*/
    private ArrayList<Commit> _sorted = new ArrayList<>();
    /** Constructor method.
     * @param current The current commit.
     * @param history The history of commits.*/
    public Tree(Commit current, TreeMap<String, Commit> history) {
        _current = current;
        _history = history;
        _history.put(current.getHash(), current);
    }
    public Commit last() {
        return _current;
    }

    public void add(Commit commit) {
        commit.setParent(_current);
        _history.put(commit.getHash(), commit);
        _current = commit;
        _sorted.add(commit);
        saveCommit();
    }

    public void rm(String filename) {
        _current.rm(filename);
        _history.replace(_current.getHash(), _current);
    }

    public Blob findCurrent(String filename) {
        return _current.find(filename);
    }

    public Commit findCommit(String hash) {
        Collection<Commit> commits = _history.values();
        Commit search = null;
        for (Commit a: commits) {
            if (a.getHash().contains(hash)) {
                search = a;
            }
        }
        if (search == null) {
            System.out.println("No commit with that id exists.");
            System.exit(0);
        }
        return search;
    }

    public boolean exists(String filename) {
        return _current.find(filename) != null;
    }

    public void saveCommit() {
        Utils.writeObject(Main.COMMITS, this);
    }

    public ArrayList<String> find(String message) {
        ArrayList<String> commitid = new ArrayList<>();
        Collection<Commit> commits = _history.values();

        for (Commit i : commits) {
            if (i.getMessage().equals(message)) {
                commitid.add(i.getHash());
            }
        }
        return commitid;
    }

    public void setCurrent(Commit current) {
        _current = current;
    }


    public Collection<Commit> getValues() {
        return _history.values();
    }

    public Commit getCurrent() {
        return _current;
    }

    @Override
    public String toString() {
        return _history.toString();
    }
}
