package gitlet;
import java.util.Date;
import java.util.TreeMap;
import java.io.Serializable;
import java.util.Map;
import java.util.Set;
import java.util.concurrent.TimeUnit;


public class Commit implements Serializable {

    /** A treemap of the files.*/
    private TreeMap<String, Blob> _files;

    /** The time the commit was made.*/
    private Date _time;

    /** The hash of the parent commit.*/
    private String _parentHash;

    /** The current commit's hash.*/
    private String _hash;

    /** The current commit's message.*/
    private String _message;

    /** The second parent, used for merge.*/
    private String _hash2;

    /** Constructor method for a commit.
     * @param files The files that the commit is tracking.
     * @param parent The parent commit. This is null on the initial commit.
     * @param message The commit message.*/
    public Commit(TreeMap<String, Blob> files, Commit parent, String message) {
        _files = files;
        _message = message;
        if (parent == null) {
            _time = new Date(0);
            _parentHash = null;
        } else {
            _parentHash = parent.getHash();
            try {
                TimeUnit.SECONDS.sleep(1);
            } catch (Exception e) {
                _time = new Date();
            }
            _time = new Date();
        }
        _hash = Utils.sha1(_time.toString());
    }

    public String getMessage() {
        return _message;
    }

    public String getHash() {
        return _hash;
    }

    public String getParent() {
        return _parentHash;
    }

    public Date getTime() {
        return _time;
    }

    public void rm(String filename) {
        _files.remove(filename);
    }

    public void setParent(Commit parent) {
        _parentHash = parent.getHash();
    }

    public Blob find(String filename) {
        return _files.get(filename);
    }
    public void setHash2(Commit commit) {
        _hash2 = commit.getHash();
    }

    public boolean hasParent() {
        return _parentHash != null;
    }

    public Set<String> files() {
        return _files.keySet();
    }

    public Set<Map.Entry<String, Blob>> map() {
        return _files.entrySet();
    }

    public TreeMap<String, Blob> fileMap() {
        return _files;
    }

    @Override
    public String toString() {
        return _message;
    }





}
