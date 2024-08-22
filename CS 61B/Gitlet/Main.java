package gitlet;
import java.io.File;
import java.util.Collection;
import java.util.Set;
import java.util.ArrayList;
import java.util.TreeMap;
import java.util.List;
import java.util.TimeZone;
import java.util.Map;
import java.util.Iterator;
import java.text.SimpleDateFormat;
import java.util.Date;
/** Driver class for Gitlet, the tiny stupid version-control system.
 *  @author Yutong Du
 */
public class Main {

    /** The file folders that we need. */
    static final File CWD = new File(System.getProperty("user.dir"));

    /** The gitlet folder.*/
    static final File GITLET = Utils.join(CWD, "/.gitlet");

    /** The log folder.*/
    static final File LOG = Utils.join(GITLET, "/log");
    /** The stage.*/
    static final File STAGE = Utils.join(GITLET, "/staging");

    /** Filepath for the commits.*/
    static final File COMMITS = Utils.join(GITLET, "/commits");

    /** Filepath for the branches.*/
    static final File BRANCH = Utils.join(GITLET, "/branches");


    /** The stage object.*/
    private static Stage _stage;

    /** The commit history.*/
    private static Tree _commithistory;

    /** The branches.*/
    private static Branch _branches;

    /** Usage: java gitlet.Main ARGS, where ARGS contains
     *  <COMMAND> <OPERAND> .... */
    public static void main(String... args) {
        if (args.length == 0) {
            System.out.println("Please enter a command.");
            System.exit(0);
        }
        if (!GITLET.exists() && !args[0].equals("init")) {
            System.out.println("Not in an initialized Gitlet directory.");
            System.exit(0);
        }
        if (args[0].equals("init")) {
            init(args);
            System.exit(0);
        } else {
            _commithistory = Utils.readObject(COMMITS, Tree.class);
            _stage = Utils.readObject(STAGE, Stage.class);
            _branches = Utils.readObject(BRANCH, Branch.class);
            switch (args[0]) {
            case "add":
                add(args);
                break;
            case "commit":
                commit(args[1]);
                break;
            case "rm":
                remove(args[1]);
                break;
            case "log":
                log();
                break;
            case "global-log":
                globalLog();
                break;
            case "checkout":
                checkout(args);
                break;
            case "find":
                find(args[1]);
                break;
            case "status":
                status();
                break;
            case "branch":
                branch(args[1]);
                break;
            case "rm-branch":
                removeBranch(args[1]);
                break;
            case "merge":
                merge(args[1]);
                break;
            case "reset":
                reset(args[1]);
            default:
                System.out.println("No command with that name exists.");
                System.exit(0);
            }
        }
    }

    public static void init(String [] args) {
        if (!(GITLET.exists() || LOG.exists() || STAGE.exists())) {
            GITLET.mkdirs();
            _stage = new Stage();
            _stage.save();
            Commit initial = new Commit(new TreeMap<>(), null,
                    "initial commit");
            _commithistory = new Tree(initial, new TreeMap<>());
            _commithistory.saveCommit();
            _branches = new Branch("master", initial);
            _branches.save();
        } else {
            System.out.println("A Gitlet version-control system "
                    + "already exists in the current directory.");
        }
    }

    public static void add(String [] args) {
        _stage.add(args[1], _commithistory.getCurrent());
    }

    public static void commit(String message) {
        if (message.equals("")) {
            System.out.println("Please enter a commit message.");
            System.exit(0);
        }
        Set<Map.Entry<String, Blob>> addFiles = _stage.getAddSet();
        Iterator<Map.Entry<String, Blob>> iter1 = addFiles.iterator();
        Set<Map.Entry<String, Blob>> rmFiles = _stage.getRemoveSet();
        Iterator<Map.Entry<String, Blob>> iter2 = rmFiles.iterator();
        Map.Entry<String, Blob> next;
        TreeMap<String, Blob> commitSave = new TreeMap<>();
        while (iter1.hasNext()) {
            next = iter1.next();
            Blob file = next.getValue();
            commitSave.put(next.getKey(), file);
        }
        while (iter2.hasNext()) {
            next = iter2.next();
            String file = next.getKey();
            _commithistory.rm(file);
        }
        Set<Map.Entry<String, Blob>> remaining
                = _commithistory.getCurrent().map();
        if (!commitSave.isEmpty() || !rmFiles.isEmpty()) {
            for (Map.Entry<String, Blob> map: remaining) {
                if (!commitSave.containsKey(map.getKey())) {
                    commitSave.put(map.getKey(), map.getValue());
                }
            }
            Commit recent = new Commit(commitSave,
                    _branches.getCurrentCommit(), message);
            _commithistory.add(recent);
            _branches.updateBranch(_branches.getCurrent(),
                    _commithistory.last());
            _stage.clear();
        } else {
            System.out.println("No changes added to the commit.");
            System.exit(0);
        }
    }

    public static void remove(String filename) {
        if (!_stage.contains(filename)
                && !_commithistory.exists(filename)) {
            System.out.println("No reason to remove the file.");
            System.exit(0);
        }

        _stage.stageRemove(filename, _commithistory.exists(filename));
    }


    public static void checkout(String[] args) {
        if (args.length == 3) {
            Blob file = _commithistory.findCurrent(args[2]);
            if (file == null) {
                System.out.println("File does not exist in that commit.");
                return;
            }
            File saved = Utils.join(CWD, args[2]);
            Utils.writeContents(saved, file.toString());
        } else if (args.length == 4) {
            if (!args[2].equals("--")) {
                System.out.println("Incorrect operands.");
            }
            Commit search = _commithistory.findCommit(args[1]);
            Blob file = search.find(args[3]);
            if (file == null) {
                System.out.println("File does not exist in that commit.");
                System.exit(0);
            }
            File saved = Utils.join(CWD, args[3]);
            Utils.writeContents(saved, file.toString());
        } else {
            if (args[1].equals(_branches.getCurrent())) {
                System.out.println("No need to checkout the current branch.");
                System.exit(0);
            } else if (!_branches.contains(args[1])) {
                System.out.println("No such branch exists.");
                System.exit(0);
            } else {
                List<String> cwdFiles = Utils.plainFilenamesIn(CWD);
                Commit commit = _branches.getCommit(args[1]);
                Commit currCommit = _branches.getCurrentCommit();
                Set<String> branchfiles = commit.files();
                Set<String> commitFiles = currCommit.files();
                for (String i : cwdFiles) {
                    if (_branches.getCurrentCommit().find(i) == null
                            && !_stage.contains(i)) {
                        System.out.println("There is an untracked file "
                                + "in the way; delete it, or add "
                                + "and commit it first.");
                        System.exit(0);
                    }
                }
                for (String file : commitFiles) {
                    if (!branchfiles.contains(file)) {
                        Utils.restrictedDelete(file);
                    }
                }
                for (String file : branchfiles) {
                    File a = new File(file);
                    Utils.writeContents(a, commit.find(file).toString());
                }

                _branches.setCurrent(args[1]);
                _stage.clear();
                _commithistory.setCurrent(_branches.getCurrentCommit());
                _commithistory.saveCommit();
            }
        }
    }

    public static void log() {
        Commit currentCommit = _branches.getCurrentCommit();
        String message = "";
        SimpleDateFormat format
                = new SimpleDateFormat("EEE MMM dd HH:mm:ss yyyy Z");
        format.setTimeZone(TimeZone.getTimeZone("PST"));
        Date date;
        String time;
        String formatted;

        while (currentCommit.hasParent()) {
            String hash = currentCommit.getHash();
            String cmessage = currentCommit.getMessage();
            date = currentCommit.getTime();
            time = format.format(date);
            formatted = time.replace(".", "");
            message += "===\r\ncommit " + hash + "\r\n"
                    + "Date: " + formatted + " \r\n"
                   + cmessage + "\r\n\r\n";
            currentCommit =
                    _commithistory.findCommit(currentCommit.getParent());
        }

        date = currentCommit.getTime();
        time = format.format(date);
        formatted = time.replace(".", "");
        message += "===\ncommit " + currentCommit.getHash() + "\n"
               + "Date: " + formatted + "\n"
                + currentCommit.getMessage() + "\n";
        System.out.println(message);
    }

    public static void globalLog() {
        Collection<Commit> commits = _commithistory.getValues();
        Iterator<Commit> iter = commits.iterator();
        Date date;
        String time;
        String formatted;
        Commit next;

        String message = "";
        SimpleDateFormat format
                = new SimpleDateFormat("EEE MMM dd HH:mm:ss yyyy Z");
        format.setTimeZone(TimeZone.getTimeZone("PST"));

        while (iter.hasNext()) {
            next = iter.next();
            date = next.getTime();
            time = format.format(date);
            formatted = time.replace(".", "");

            message += "===\ncommit " + next.getHash() + "\n"
                    + "Date: " + formatted + "\n"
                    + next.getMessage() + "\n\n";
        }

        System.out.println(message);
    }

    public static void find(String message) {
        ArrayList<String> commits = _commithistory.find(message);

        if (commits.size() == 0) {
            System.out.println("Found no commit with that message.");
            return;
        }
        for (String i : commits) {
            System.out.println(i);
        }
    }

    public static void status() {
        String message = "=== Branches ===" + "\n";
        Set<String> branches = _branches.getBranches();
        ArrayList<String> stageAdd = _stage.getAddKeys();
        ArrayList<String> stageRemove = _stage.getRemoveKeys();
        for (String i : branches) {
            if (i.equals(_branches.getCurrent())) {
                message += "*" + i + "\n";
            } else {
                message += i + "\n";
            }
        }
        message += "\n=== Staged Files ===\n";
        for (String file : stageAdd) {
            message += file + "\n";
        }
        message += "\n=== Removed Files ===\n";
        for (String file: stageRemove) {
            message += file + "\n";
        }
        message += "\n=== Modifications Not Staged For Commit ===\n";
        Commit currCommit = _branches.getCurrentCommit();
        Set<Map.Entry<String, Blob>> files = currCommit.map();
        List<String> cwdFiles = Utils.plainFilenamesIn(CWD);
        for (Map.Entry<String, Blob> a : files) {
            try {
                Blob file = a.getValue();
                String filecontents = Utils.readContentsAsString(
                        Utils.join(CWD, a.getKey()));
                if (!file.toString().equals(filecontents)) {
                    message += a.getKey() + "\n";
                }
            } catch (IllegalArgumentException e) {
                message += "";
            }
        }
        message += "\n=== Untracked Files ===\n";

        for (String i :cwdFiles) {
            if (_branches.getCurrentCommit().find(i) == null
                    && !_stage.contains(i)) {
                message += i + "\n";
            }
        }
        System.out.println(message);
    }

    public static void branch(String branchname) {
        if (_branches.contains(branchname)) {
            System.out.println("A branch with that name already exists.");
            System.exit(0);
        }
        _branches.updateBranch(branchname, _commithistory.getCurrent());
    }

    public static void reset(String commitid) {
        Collection<Commit> commits
                = _commithistory.getValues();
        Commit search = null;
        for (Commit a: commits) {
            if (a.getHash().contains(commitid)) {
                search = a;
                break;
            }
        }
        if (search == null) {
            System.out.println("No commit with that id exists");
            System.exit(0);
        }
        List<String> cwdFiles = Utils.plainFilenamesIn(CWD);
        Set<String> files = search.files();
        for (String file : cwdFiles) {
            if (!files.contains(file)) {
                System.out.println("There is an untracked file in the "
                        + "way; delete it, or add and commit it first.");
            }
            System.exit(0);
        }
        for (String filename: files) {
            checkout(new String[]{"checkout",
                    search.getHash(), " -- ", filename});
        }
        _branches.setCurrent(search.getHash());
    }

    public static void removeBranch(String branchname) {
        if (branchname.equals(_branches.getCurrent())) {
            System.out.println("Cannot remove the current branch.");
            System.exit(0);
        } else if (!_branches.contains(branchname)) {
            System.out.println("A branch with that name does not exist.");
        } else {
            _branches.removeBranch(branchname);
        }
        _branches.save();
    }


    public static void mergeErrors(String branchname) {
        List<String> cwdFiles = Utils.plainFilenamesIn(CWD);
        Set<String> files = _branches.getCurrentCommit().files();
        for (String i :cwdFiles) {
            if (!files.contains(i) && !_stage.contains(i)) {
                System.out.println("There is an untracked file in the way; "
                        + "delete it, or add and commit it first.");
            }
            System.exit(0);
        }

        if (branchname.equals(_branches.getCurrent())) {
            System.out.println("Cannot merge a branch with itself.");
            System.exit(0);
        } else if (!_stage.isEmpty()) {
            System.out.println("You have uncommitted changes");
            System.exit(0);
        }
    }

    public static void merge(String branchname) {
        mergeErrors(branchname);
        Commit givenCommit = _branches.getCommit(branchname);
        Commit currentCommit = _branches.getCurrentCommit();
        boolean conflict = false;
        ArrayList<Commit> givenParents = new ArrayList<>();
        while (currentCommit.hasParent()) {
            givenParents.add(
                    _commithistory.findCommit(currentCommit.getParent()));
            currentCommit =
                    _commithistory.findCommit(currentCommit.getParent());
        }
        while (givenCommit.hasParent()) {
            if (givenParents.contains(
                    _commithistory.findCommit(
                            givenCommit.getParent()))) {
                givenCommit = _commithistory.findCommit(
                        givenCommit.getParent());
                break;
            }
            givenCommit = _commithistory.findCommit(
                    givenCommit.getParent());
        }
        Commit ancestor = givenCommit;
        System.out.println(ancestor.getMessage());
        givenCommit = _branches.getCommit(branchname);

        Set<Map.Entry<String, Blob>> currentMap
                = _commithistory.getCurrent().map();
        Set<Map.Entry<String, Blob>> givenMap
                = givenCommit.map();
        String givenContents, currentContents, ancestorContents;
        for (Map.Entry<String, Blob> file: givenMap) {
            givenContents = file.getValue().getHash();
            currentContents = _branches.getCurrentCommit()
                    .find(file.getKey()).getHash();
            ancestorContents = ancestor.find(file.getKey()).getHash();
            if (currentContents.equals(ancestorContents)) {
                if (givenContents.equals("")) {
                    Utils.restrictedDelete(file.getKey());
                } else if (!givenContents.equals(currentContents)) {
                    File a = Utils.join(CWD, file.getKey());
                    Utils.writeContents(a, file.getValue().toString());
                }
            }
        }
        if (conflict) {
            System.out.println("Encountered a merge conflict.");
        }
        commit("Merged" + branchname + "into" + _branches.getCurrent());
        _commithistory.getCurrent().setHash2(_branches.getCommit(branchname));
        _commithistory.saveCommit();
    }
}
