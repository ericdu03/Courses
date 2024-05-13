package gitlet;
import java.util.TreeMap;
import java.io.Serializable;
import java.io.File;
import java.util.Map;
import java.util.Set;
import java.util.ArrayList;

public class Stage implements Serializable {

    /** The stage for additions.*/
    private TreeMap<String, Blob>
            _stageAdd = new TreeMap<>();

    /** The stage for removals.*/
    private TreeMap<String, Blob>
            _stageRemove = new TreeMap<>();
    /** A stage object. Stores only a temporary TreeMap
     * and saves it as a file in .gitlet, so that it may
     * be read in later and accessed. Since the stage
     * object only stores temporary information about files,
     * we only need to store the TreeMap.
     */

    public Stage() {
    }

    public void add(String filename, Commit commit) {
        File search = Utils.join(Main.CWD, filename);
        try {
            String file = Utils.readContentsAsString(search);
            Blob toBeStaged = new Blob(file);
            Blob commitBlob = commit.find(filename);

            if (commitBlob != null
                    && !_stageRemove.containsKey(filename)) {
                if (commitBlob.getHash().
                        equals(toBeStaged.getHash())) {
                    return;
                }
            }

            if (_stageAdd.containsKey(filename)
                    && !toBeStaged.getHash().equals(commitBlob.getHash())) {
                _stageAdd.put(filename, toBeStaged);
            } else if (_stageAdd.containsKey(filename)
                    && !toBeStaged.getHash().
                    equals(_stageAdd.get(filename).toString())) {
                _stageAdd.put(filename, toBeStaged);
            } else if (!_stageAdd.containsKey(filename)
                    && !_stageRemove.containsKey(filename)) {
                _stageAdd.put(filename, toBeStaged);
            } else if (_stageRemove.containsKey(filename)
                    && !_stageAdd.containsKey(filename)) {
                _stageRemove.remove(filename);
            }
            _stageRemove.remove(filename);
        } catch (IllegalArgumentException e) {
            Blob removal = _stageRemove.remove(filename);

            if (removal == null) {
                System.out.println("File does not exist.");
            }
        }
        save();
    }

    public void singleRemove(String filename) {
        _stageRemove.remove(filename);
    }

    public void stageRemove(String filename, Boolean inCommit) {
        _stageAdd.remove(filename);
        if (inCommit) {
            _stageRemove.put(filename, _stageAdd.get(filename));
            Utils.restrictedDelete(Utils.join(Main.CWD, filename));
        }
        save();
    }

    public void clear() {
        _stageAdd.clear();
        _stageRemove.clear();
        save();
    }

    public boolean isEmpty() {
        return _stageAdd.isEmpty() && _stageRemove.isEmpty();
    }

    public boolean contains(String filename) {
        return _stageAdd.containsKey(filename)
                || _stageRemove.containsKey(filename);
    }

    public Set<Map.Entry<String, Blob>> getAddSet() {
        return _stageAdd.entrySet();
    }

    public Set<Map.Entry<String, Blob>> getRemoveSet() {
        return _stageRemove.entrySet();
    }

    public ArrayList<String> getAddKeys() {
        ArrayList<String> result = new ArrayList<>();
        Set<String> keys = _stageAdd.keySet();

        for (String key: keys) {
            result.add(key);
        }
        return result;

    }
    public ArrayList<String> getRemoveKeys() {
        ArrayList<String> result = new ArrayList<>();
        Set<String> keys = _stageRemove.keySet();

        for (String key: keys) {
            result.add(key);
        }
        return result;
    }

    @Override
    public String toString() {
        return _stageAdd.toString();
    }

    public void save() {
        Utils.writeObject(Main.STAGE, this);
    }
}
