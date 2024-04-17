# Copyright 2023-2024 DreamWorks Animation LLC and Intel Corporation
# SPDX-License-Identifier: Apache-2.0

function(ArrasNode_cxx_compile_definitions target)
    target_compile_definitions(${target}
        PRIVATE
            _LIBCPP_ENABLE_CXX17_REMOVED_UNARY_BINARY_FUNCTION # Boost headers refer to unary_function, which was apparently removed in C++ 17

            $<$<CONFIG:DEBUG>:
                DEBUG                               # Enables extra validation/debugging code
            >
            $<$<CONFIG:RELWITHDEBINFO>:
                BOOST_DISABLE_ASSERTS               # Disable BOOST_ASSERT macro
            >
            $<$<CONFIG:RELEASE>:
                BOOST_DISABLE_ASSERTS               # Disable BOOST_ASSERT macro
            >

        PUBLIC
            ${GLOBAL_COMPILE_DEFINITIONS}
            GL_GLEXT_PROTOTYPES=1                   # This define makes function symbols to be available as extern declarations.
            TBB_SUPPRESS_DEPRECATED_MESSAGES        # Suppress 'deprecated' messages from TBB
    )
endfunction()

