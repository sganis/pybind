#!/bin/sh
#
# check code style with cpplint.py

if [ $# -lt 1 ];then
	echo "usage: $0 <project-path>"
	exit 1
fi

DIR="$( cd "$( dirname "$0" )" && pwd )"

echo "running cpplint.py $1 ..."
find $1 -type f \( -name "*.h" -o -name "*.cpp" \) \
	| grep -v "\.lex\.\|\.yac\." \
	| xargs $DIR/cpplint.py \
	--linelength=80 \
	--filter=-build/c++11,-build/header_guard,-build/include,-runtime/references,-readability/casting \
	--output=eclipse

echo "exit code from lint: $?"

# overwrite exit code so we can run this script after build 
# and warnings don't stop build
exit 0

# filters used by cpplint.py:
# ---------------------------
# build/class                                  
# build/c++11                                  
# build/c++14                                  
# build/c++tr1                                 
# build/deprecated                             
# build/endif_comment                          
# build/explicit_make_pair                     
# build/forward_decl                           
# build/header_guard                           
# build/include                                
# build/include_alpha                          
# build/include_order                          
# build/include_what_you_use                   
# build/namespaces                             
# build/printf_format                          
# build/storage_class                          
# legal/copyright                              
# readability/alt_tokens                       
# readability/braces                           
# readability/casting                          
# readability/check                            
# readability/constructors                     
# readability/fn_size
# readability/inheritance
# readability/multiline_comment
# readability/multiline_string
# readability/namespace
# readability/nolint
# readability/nul
# readability/strings
# readability/todo
# readability/utf8
# runtime/arrays
# runtime/casting
# runtime/explicit
# runtime/int
# runtime/init
# runtime/invalid_increment
# runtime/member_string_references
# runtime/memset
# runtime/indentation_namespace
# runtime/operator
# runtime/printf
# runtime/printf_format
# runtime/references
# runtime/string
# runtime/threadsafe_fn
# runtime/vlog
# whitespace/blank_line
# whitespace/braces
# whitespace/comma
# whitespace/comments
# whitespace/empty_conditional_body
# whitespace/empty_if_body
# whitespace/empty_loop_body
# whitespace/end_of_line
# whitespace/ending_newline
# whitespace/forcolon
# whitespace/indent
# whitespace/line_length
# whitespace/newline
# whitespace/operators
# whitespace/parens
# whitespace/semicolon
# whitespace/tab
# whitespace/todo
