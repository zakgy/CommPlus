package com.example.commplus;

import android.app.FragmentTransaction;
import android.os.Bundle;
import android.widget.TextView;

import androidx.appcompat.app.AppCompatActivity;

public class MainActivity extends AppCompatActivity {
    String SENTENCE = "";

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        // Begin the transaction
        FragmentTransaction ft = getFragmentManager().beginTransaction();
        // Add the contents of the container with the new fragment
        ft.add(R.id.fragment_container, new fragment0());
        // Complete the changes added above
        ft.commit();
    }

    // Concatenates new_word to the end of SENTENCE, then sets sentence_bar to SENTENCE
    // Called by onClick from all fragment buttons
    void update_sentence_bar(String new_word) {
        if (!SENTENCE.equals("")) {
            SENTENCE += " --> ";
        }
        SENTENCE += new_word;
        TextView sentence_bar = (TextView) findViewById(R.id.sentence_bar);
        sentence_bar.setText(SENTENCE);
    }

    // Sets SENTENCE to "", then sets sentence_bar to SENTENCE
    void clear_sentence_bar() {
        SENTENCE = "";
        TextView sentence_bar = (TextView) findViewById(R.id.sentence_bar);
        sentence_bar.setText(SENTENCE);
    }
}
