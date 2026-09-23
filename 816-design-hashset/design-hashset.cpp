class MyHashSet {
private:
    static const int bucketCount = 1000;
    vector<list<int>> buckets;
    
    int hashFunc(int key) {
        return key % bucketCount;
    }
    
public:
    MyHashSet() {
        buckets.resize(bucketCount);
    }
    
    void add(int key) {
        int idx = hashFunc(key);
        auto& bucket = buckets[idx];
        if (find(bucket.begin(), bucket.end(), key) == bucket.end()) {
            bucket.push_back(key);
        }
    }
    
    void remove(int key) {
        int idx = hashFunc(key);
        auto& bucket = buckets[idx];
        bucket.remove(key); // std::list::remove removes all matching elements
    }
    
    bool contains(int key) {
        int idx = hashFunc(key);
        auto& bucket = buckets[idx];
        return find(bucket.begin(), bucket.end(), key) != bucket.end();
    }
};

/**
 * Your MyHashSet object will be instantiated and called as such:
 * MyHashSet* obj = new MyHashSet();
 * obj->add(key);
 * obj->remove(key);
 * bool param_3 = obj->contains(key);
 */