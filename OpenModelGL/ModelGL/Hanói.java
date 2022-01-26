import java.util.Stack;

public class Towers {
    private static final int DEFAULT_SIZE = 5;
    private static final int MAX_SIZE = 64;
    private static final int MIN_PEG = 1;
    private static final int MAX_PEG = 3;
    private static Stack<Integer>[] tower = new Stack[4];
    private int numOfRings;

public Towers(int n) {
    if (n < 1 || n > MAX_SIZE) 
        throw new IllegalArgumentException(
                String.format("Number of rings (%s) cannot be less than 1 or exceed 64 ", n));
    numOfRings = n;
    tower[1] = new Stack<Integer>();
    tower[2] = new Stack<Integer>();
    tower[3] = new Stack<Integer>();
    for (int i = 1; i <= numOfRings; i++)
        tower[1].push(i);
}
public Towers() {
    numOfRings = DEFAULT_SIZE;
    tower[1] = new Stack<Integer>();
    tower[2] = new Stack<Integer>();
    tower[3] = new Stack<Integer>();
    for (int i = 1; i <= numOfRings; i++)
        tower[1].push(i);
}

private static void pegCheck(int pegNumber){
    if (pegNumber < MIN_PEG || pegNumber > MAX_PEG) 
        throw new IllegalArgumentException(
                String.format("Peg number (%s) cannot be less than 1 or exceed 3 ", pegNumber));
}
public int getRingCount(int pegNumber) {
    pegCheck(pegNumber);

    switch (pegNumber) {
    case 1:
        if (tower[1].isEmpty()) 
            return 0;
        else 
            return tower[1].size();
    case 2:
        if (tower[2].isEmpty()) 
            return 0;
        else 
            return tower[2].size();
    case 3:
        if (tower[3].isEmpty()) 
            return 0;
        else 
            return tower[3].size();
    default:
        return 0;
    }
}
public int getTopDiameter(int pegNumber) {
    pegCheck(pegNumber);

    switch (pegNumber) {
    case 1:
        if(getRingCount(1) > 0){
            return tower[1].get(tower[1].peek() - tower[1].size());
        }else
            return 0;
    case 2:
        if(getRingCount(2) > 0){
            return tower[2].get(tower[2].peek() - tower[2].size());
        }else
            return 0;
    case 3:
        if(getRingCount(3) > 0){
            return tower[3].get(tower[3].peek() - tower[3].size());
        }else
            return 0;
    default:
        return 0;
    }
}
public boolean move(int startPeg, int endPeg) {
    pegCheck(startPeg);
    pegCheck(endPeg);
    Stack<Integer> startTower = tower[startPeg];
    Stack<Integer> endTower = tower[endPeg];


    if (getRingCount(startPeg) > 0 && endPeg != startPeg && getRingCount(endPeg) > 0 && getTopDiameter(startPeg) < getTopDiameter(endPeg)) {
        int topRing = startTower.pop();
        endTower.push(topRing);
        return true;import static org.junit.Assert.*;
import org.junit.Test;
import edu.metrostate.ics240.p2.towers.*;
import java.util.Random;

public class TowersTest {
    private static final int MAX_NUM_RINGS = 64;
    private static final long SEED = 20170604001L;
    private static final Random RAND = new Random(SEED);

@Test
public void testDefaultConstruction() {
    Towers t = new Towers();
    assertEquals(5, t.getRingCount(1));
    assertEquals(0, t.getRingCount(2));
    assertEquals(0, t.getRingCount(3));

    assertEquals(1, t.getTopDiameter(1));
    assertEquals(0, t.getTopDiameter(2));
    assertEquals(0, t.getTopDiameter(3));
}

@Test
public void testConstruction() {
    int numRings = RAND.nextInt(MAX_NUM_RINGS);
    Towers t = new Towers(numRings);
    assertEquals(numRings, t.getRingCount(1));
    assertEquals(0, t.getRingCount(2));
    assertEquals(0, t.getRingCount(3));

    assertEquals(1, t.getTopDiameter(1));
    assertEquals(0, t.getTopDiameter(2));
    assertEquals(0, t.getTopDiameter(3));
}

@Test
public void testMove() {
    int numRings = RAND.nextInt(64);

    Towers t = new Towers(numRings);

    assertTrue(t.move(1, 2));
    assertEquals(numRings - 1, t.getRingCount(1));
    assertEquals(1, t.getRingCount(2));
    assertEquals(0, t.getRingCount(3));

    assertEquals(2, t.getTopDiameter(1));
    assertEquals(1, t.getTopDiameter(2));
    assertEquals(0, t.getTopDiameter(3));

    assertTrue(t.move(1, 3));
    assertEquals(numRings - 2, t.getRingCount(1));
    assertEquals(1, t.getRingCount(2));
    assertEquals(1, t.getRingCount(3));

    assertEquals(3, t.getTopDiameter(1));
    assertEquals(1, t.getTopDiameter(2));
    assertEquals(2, t.getTopDiameter(3));
}

@Test
public void testInvalidConstructor(){
    Towers t = null;
    try {
        t = new Towers(0); // illegal value
        fail("Expected exception");
    } catch (IllegalArgumentException iae) {
        // expected
    }

    try {
        t = new Towers(MAX_NUM_RINGS + 1); // illegal value
        fail("Expected exception");
    } catch (IllegalArgumentException iae) {
        // expected
    }
}
@Test
public void testPreconditionGetRingCount() {
    Towers t = new Towers();
    try {
        t.getRingCount(0);
        fail("Exception expected");
    } catch (IllegalArgumentException iae) {
        // expected
    }
    try {
        t.getRingCount(4);
        fail("Exception expected");
    } catch (IllegalArgumentException iae) {
        // expected
    }
}

@Test
public void testPreconditionTopRing() {
    Towers t = new Towers();
    try {
        t.getTopDiameter(0);
        fail("Exception expected");
    } catch (IllegalArgumentException iae) {
        // expected
    }
    try {
        t.getTopDiameter(4);
        fail("Exception expected");
    } catch (IllegalArgumentException iae) {
        // expected
    }
}

@Test
public void testIllegalMoves(){
    Towers t = new Towers();

    t.move(1, 2);
    t.move(1, 3);

    assertFalse(t.move(1, 1)); // can't move to itself
    assertFalse(t.move(1, 2)); // moving larger ring to smaller
    assertFalse(t.move(1, 3)); // moving larger ring to smaller
    assertFalse(t.move(3, 2));
}
}
    }else  
    import java.util.Stack;

public class Towers {
    private static final int DEFAULT_SIZE = 5;
    private static final int MAX_SIZE = 64;
    private static final int MIN_PEG = 1;
    private static final int MAX_PEG = 3;
    @SuppressWarnings("unchecked")
    private static Stack<Integer>[] tower = new Stack[4];
    private int numOfRings;

public Towers(int n) {
    if (n < 1 || n > MAX_SIZE)
        throw new IllegalArgumentException(
                String.format("Number of rings (%s) cannot be less than 1 or exceed 64 ", n));
    numOfRings = n;
    tower[1] = new Stack<Integer>();
    tower[2] = new Stack<Integer>();
    tower[3] = new Stack<Integer>();
    for (int i = numOfRings; i >= 1; i--)
        tower[1].push(i);
}

public Towers() {
    numOfRings = DEFAULT_SIZE;
    tower[1] = new Stack<Integer>();
    tower[2] = new Stack<Integer>();
    tower[3] = new Stack<Integer>();
    for (int i = numOfRings; i >= 1; i--)
        tower[1].push(i);
}

private static void pegCheck(int pegNumber) {
    if (pegNumber < MIN_PEG || pegNumber > MAX_PEG)
        throw new IllegalArgumentException(
                String.format("Peg number (%s) cannot be less than 1 or exceed 3 ", pegNumber));
}

public int getRingCount(int pegNumber) {
    pegCheck(pegNumber);
    if (tower[pegNumber].isEmpty()) {
        return 0;
    } else
        return tower[pegNumber].size();
}

public int getTopDiameter(int pegNumber) {
    pegCheck(pegNumber);
    if (getRingCount(pegNumber) > 0) {
        return tower[pegNumber].get(tower[pegNumber].size() - 1);
    }
    return 0;
}

public boolean move(int startPeg, int endPeg) {
    pegCheck(startPeg);
    pegCheck(endPeg);

    if (endPeg != startPeg) {
        if (getRingCount(startPeg) > 0) {
            if (getRingCount(endPeg) == 0 || getTopDiameter(startPeg) < getTopDiameter(endPeg)) {
                int topRing = tower[startPeg].pop();
                tower[endPeg].push(topRing);
                return true;
            }

        }
    }
    return false;
}
}
        return false;
}
} 
