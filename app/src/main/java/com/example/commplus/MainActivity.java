package com.example.commplus;

import android.app.FragmentTransaction;
import android.os.Bundle;
import android.widget.TextView;

import androidx.appcompat.app.AppCompatActivity;

import java.util.Stack;
import java.util.Vector;

public class MainActivity extends AppCompatActivity {
    Vector<String> SENTENCE = new Vector<>();

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        // Load fragment0, the tree root
        FragmentTransaction ft = getFragmentManager().beginTransaction();
        ft.add(R.id.fragment_container, new gen_fragment0());
        ft.commit();

        // Load quick buttons fragment
        ft = getFragmentManager().beginTransaction();
        ft.add(R.id.quick_buttons, new QuickButtons());
        ft.commit();
    }

    // Concatenates new_word to the end of SENTENCE, then sets sentence_bar to SENTENCE
    // Called by onClick from all fragment buttons
    void sentence_bar_write() {
        String sentence = "";
        for (int i = 0; i < SENTENCE.size(); i++) {
            sentence += SENTENCE.get(i);
            if (i != SENTENCE.size() - 1) {
                sentence += "-->";
            }
        }
        TextView sentence_bar = (TextView) findViewById(R.id.sentence_bar);
        sentence_bar.setText(sentence);
    }

    void sentence_bar_add(String new_word) {
        SENTENCE.add(new_word);
    }

    void sentence_bar_delete() {
        SENTENCE.remove(SENTENCE.size()-1);
    }

    // Sets SENTENCE to "", then sets sentence_bar to SENTENCE
    void sentence_bar_clear() {
        SENTENCE.clear();
    }
}
