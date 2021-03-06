import sys
import os
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

def findImage(images, name):
    image = 'test';
    if name in images:
        if images[name] == "":
            print("Word: " + name + " file missing");
        else:
            image = images[name];
            image = image.split('.')[0];
    else:
        print("Word: " + name + " word missing");
    return image;
    
xml_relative_layout = '<?xml version="1.0" encoding="utf-8"?>\n<RelativeLayout xmlns:android="http://schemas.android.com/apk/res/android"\n\txmlns:tools="http://schemas.android.com/tools"\n\tandroid:layout_width="match_parent"\n\tandroid:layout_height="match_parent" >\n';

## xml file generation
def create_xml (tree, images, parent):
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
            text += '\n\t\t\tandroid:text="' + tree[child] + '"';
            text += '\n\t\t\tandroid:textSize="20sp"';
            text += '\n\t\t\tandroid:drawableTop="@drawable/' + findImage(images, tree[child]) + '"';
            text += '/>\n';

    text += '\t</LinearLayout>\n';
    text += '</RelativeLayout>';
    return text;

java_imports = 'package com.example.commplus;\n';
java_imports += '\nimport android.app.Fragment;';
java_imports += '\nimport android.app.FragmentTransaction;';
java_imports += '\nimport android.graphics.Bitmap;';
java_imports += '\nimport android.graphics.drawable.BitmapDrawable;';
java_imports += '\nimport android.graphics.drawable.Drawable;';
java_imports += '\nimport android.os.Bundle;';
java_imports += '\nimport android.util.DisplayMetrics;';
java_imports += '\nimport android.view.LayoutInflater;';
java_imports += '\nimport android.view.View;';
java_imports += '\nimport android.view.ViewGroup;';
java_imports += '\nimport android.widget.Button;';

## java file generation
def create_java (tree, images, parent):
    children = getChildIds(parent);
    
    text = java_imports;
    text += '\n\npublic class gen_fragment' + str(parent) + ' extends Fragment {';
    text += '\n\tView view;\n';
    
    for child in children:
        if childExists(tree, child):
            text += '\n\tButton button_' + str(child) + ';';
        
    text += '\n\t@Override\n\tpublic View onCreateView(LayoutInflater inflater, ViewGroup container, Bundle savedInstanceState) {';
    text += '\n\t\tview = inflater.inflate(R.layout.gen_fragment_' + str(parent) + ', container, false);\n';
    text += '\n\t\tfloat SCALE_FACTOR = 100;';
    text += '\n\t\tDisplayMetrics dm = new DisplayMetrics();';
    text += '\n\t\t((MainActivity)getActivity()).getWindowManager().getDefaultDisplay().getMetrics(dm);';
    text += '\n\t\tfloat densityScale = dm.scaledDensity;';
    text += '\n\t\tfloat scaledWidth = SCALE_FACTOR * densityScale;';
    text += '\n\t\tfloat scaledHeight = SCALE_FACTOR * densityScale;';
    text += '\n\t\tDrawable dr;';
    text += '\n\t\tBitmap bitmap;';
    text += '\n\t\tDrawable d;';
    text += '\n';

    for child in children:
        if childExists(tree, child):
            dest = str(child);
            if not hasChildren(tree,child):
                dest = '0';
            text += '\n\t\tbutton_' + str(child) + ' = (Button) view.findViewById(R.id.button' + str(child) + ');';
            text += '\n\t\tdr = getResources().getDrawable(R.drawable.' + findImage(images, tree[child]) + ');';
            text += '\n\t\tbitmap = ((BitmapDrawable) dr).getBitmap();';
            text += '\n\t\td = new BitmapDrawable(this.getResources(),Bitmap.createScaledBitmap(bitmap, (int)scaledWidth, (int)scaledHeight, true));';
            text += '\n\t\tbutton_' + str(child) + '.setCompoundDrawablesWithIntrinsicBounds(null, d,null,null);';
            text += '\n\t\tbutton_' + str(child) + '.setOnClickListener(new View.OnClickListener() {';
            text += '\n\t\t\tpublic void onClick(View v) {';
            text += '\n\t\t\t\tMainActivity main_activity = (MainActivity) getActivity();';
            text += '\n\t\t\t\tString button_text = button_' + str(child) + '.getText().toString();';
            text += '\n\t\t\t\tmain_activity.sentence_bar_add(button_text);';
            text += '\n\t\t\t\tmain_activity.sentence_bar_write();';
            text += '\n';
            text += '\n\t\t\t\tFragmentTransaction ft = getFragmentManager().beginTransaction();';
            text += '\n\t\t\t\tft.replace(R.id.fragment_container, new gen_fragment' + dest + '());';
            text += '\n\t\t\t\tft.addToBackStack(null);';
            text += '\n\t\t\t\tft.commit();';
            text += '\n\t\t\t}\n\t\t});';

    text += '\n\n\t\t return view;\n\t}\n}';
    return text;

def main():
    tree = CSVtoHash(1);
    images = CSVtoHash(2);
    n_fragments = len(tree);
    
    os.system("del layouts\*");
    os.system("del java\*");
    print('Generating code for ' + str(n_fragments) + ' fragments...');
    
    print('\tGenerating XML files...');
    for fragment in range(n_fragments):
        if childExists(tree, fragment):
            if hasChildren(tree, fragment):
                filename = "layouts/gen_fragment_" + str(fragment) + ".xml";
                file = open(filename, "w");
                file.write(create_xml(tree, images, fragment));
                file.close();

    print('\tGenerating Java files...');
    for fragment in range(n_fragments):
        if childExists(tree, fragment):
            if hasChildren(tree, fragment):
                filename = "java/gen_fragment" + str(fragment) + ".java";
                file = open(filename, "w");
                file.write(create_java(tree, images, fragment));
                file.close();
    return;

def test(arg):
    tree = CSVtoHash(1);
    images = CSVtoHash(2);
    if arg == 'xml':
        print(create_xml(tree, images, 0));
        return;
    if arg == 'java':
        print(create_java(tree, images, 0));
        return;
    print(create_xml(tree, images, 0));
    print(create_java(tree, images, 0));
    
if len(sys.argv) > 1:
    if sys.argv[1] == 'write':
        main();
    else:
        test(sys.argv[1]);
else:
    test('');
