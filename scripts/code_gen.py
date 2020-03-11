import sys
from TreeHashTable import getChildIds, getChildNames, CSVtoHash;

def childExists(tree, child):
    if child >= len(tree):
        return 0;
    if tree[child] == '':
        return 0;
    return 1;

def hasChildren(tree, parent):
    children = getChildIds(parent);
    for child in children:
        if childExists(tree, child):
            return 1;
    return 0;

xml_relative_layout = '<?xml version="1.0" encoding="utf-8"?>\n<RelativeLayout xmlns:android="http://schemas.android.com/apk/res/android"\n\txmlns:tools="http://schemas.android.com/tools"\n\tandroid:layout_width="match_parent"\n\tandroid:layout_height="match_parent" >\n';

## xml file generation
def create_xml (tree, parent):
    children = getChildIds(parent);
    
    text = xml_relative_layout;
    text += '\t<LinearLayout\n\t\tandroid:layout_width="match_parent"';
    text += '\n\t\tandroid:layout_height="match_parent"';
    text += '\n\t\tandroid:layout_weight="1"';
    text += '\n\t\tandroid:orientation="horizontal"';
    text += '\n\t\tandroid:weightSum="' + str(len(children)) + '" >\n';

    for child in children:
        if childExists(tree, child):
            text += '\t\t<Button'
            text += '\n\t\t\tandroid:id="@+id/button' + str(child);
            text += '"\n\t\t\tandroid:layout_width="0dp"';
            text += '\n\t\t\tandroid:layout_height="match_parent"';
            text += '\n\t\t\tandroid:layout_weight="1"';
            text += '\n\t\t\tandroid:scaleType="fitCenter"';
            text += '\n\t\t\tandroid:text="' + tree[child] + '" />\n';

    text += '\t</LinearLayout>\n';
    text += '</RelativeLayout>';
    return text;

java_imports = 'package com.example.commplus;\n\nimport android.app.Fragment;\nimport android.app.FragmentTransaction;\nimport android.os.Bundle;\nimport android.view.LayoutInflater;\nimport android.view.View;\nimport android.view.ViewGroup;\nimport android.widget.Button;';

## java file generation
def create_java (tree, parent):
    children = getChildIds(parent);
    
    text = java_imports;
    text += '\n\npublic class fragment' + str(parent) + ' extends Fragment {';
    text += '\n\tView view;\n';
    
    for child in children:
        text += '\n\tButton button_' + str(child) + ';';
        
    text += '\n\t@Override\n\tpublic View onCreateView(LayoutInflater inflater, ViewGroup container, Bundle savedInstanceState) {';
    text += '\n\t\tview = inflater.inflate(R.layout.fragment_' + str(parent) + ', container, false);\n';

    for child in children:
        if childExists(tree, child):
            dest = str(child);
            if not hasChildren(tree,child):
                dest = '0';
            text += '\n\t\tbutton_' + str(child) + ' = (Button) view.findViewById(R.id.button' + str(child) + ');';
            text += '\n\t\tbutton_' + str(child) + '.setOnClickListener(new View.OnClickListener() {';
            text += '\n\t\t\tpublic void onClick(View v) {';
            text += '\n\t\t\t\tMainActivity main_activity = (MainActivity) getActivity();';
            text += '\n\t\t\t\tString button_text = button_' + str(child) + '.getText().toString();';
            text += '\n\t\t\t\tmain_activity.update_sentence_bar(button_text);'
            text += '\n';
            text += '\n\t\t\t\tFragmentTransaction ft = getFragmentManager().beginTransaction();';
            text += '\n\t\t\t\tft.replace(R.id.fragment_container, new fragment' + dest + '());';
            text += '\n\t\t\t\tft.addToBackStack(null);';
            text += '\n\t\t\t\tft.commit();';
            text += '\n\t\t\t}\n\t\t});';

    text += '\n\n\t\t return view;\n\t}\n}';
    return text;

def main():
    tree = CSVtoHash(1);

    n_fragments = len(tree);
    print('Generating code for ' + str(n_fragments) + ' fragments...');
    
    print('\tGenerating XML files...');
    for fragment in range(n_fragments):
        if childExists(tree, fragment):
            if hasChildren(tree, fragment):
                filename = "layouts/fragment_" + str(fragment) + ".xml";
                file = open(filename, "w");
                file.write(create_xml(tree, fragment));
                file.close();

    print('\tGenerating Java files...');
    for fragment in range(n_fragments):
        if childExists(tree, fragment):
            if hasChildren(tree, fragment):
                filename = "java/fragment" + str(fragment) + ".java";
                file = open(filename, "w");
                file.write(create_java(tree, fragment));
                file.close();
    return;

def test(arg):
    tree = CSVtoHash(1);
    if arg == 'xml':
        print(create_xml(tree, 0));
        return;
    if arg == 'java':
        print(create_java(tree, 0));
        return;
    print(create_xml(tree, 0));
    print(create_java(tree, 0));
    
if len(sys.argv) > 1:
    if sys.argv[1] == 'write':
        main();
    else:
        test(sys.argv[1]);
else:
    test('');
